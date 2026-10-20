import os
import re
import markdown
import subprocess

report_dir = r"C:\Users\visha\Downloads\New folder (2)\mlops-assign\report"
md_path = os.path.join(report_dir, "REPORT.md")
html_path = os.path.join(report_dir, "REPORT.html")
pdf_out = os.path.join(report_dir, "REPORT_SUBMISSION.pdf")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Make links fully clickable and prevent breaking into multiple lines
video_url = "https://drive.google.com/file/d/1Ge0n5zKUrra-930hwrPkaRZR9Ma7kfvB/view?usp=sharing"
github_url = "https://github.com/VishalAnand07/MLOps_Assigment_1_2025AE05692"

# Replace markdown image patterns with cards
def clean_img(m):
    alt = m.group(1)
    src = m.group(2)
    w = m.group(3)
    return (
        f'<div class="figure-card">'
        f'<img src="{src}" style="width:{w}%;" alt="{alt}"/>'
        f'<div class="figure-caption"><span>Figure:</span> {alt}</div>'
        f'</div>'
    )

text = re.sub(r"!\[(.*?)\]\((.*?)\)\{width=(\d+)%\}", clean_img, text)

# Convert to html
body_html = markdown.markdown(text, extensions=["tables", "fenced_code"])

# Post-process the metadata header paragraph so links are clean, single-line, and clickable
body_html = re.sub(
    r'(\*\*Demo video:\*\*\s*)(`?https://drive\.google\.com/[^\s<`]+`?)',
    f'<strong>Demo video:</strong> <a href="{video_url}" class="no-break-link" target="_blank">{video_url}</a>',
    body_html
)

body_html = re.sub(
    r'(\*\*Code repository:\*\*\s*)(`?https://github\.com/[^\s<`]+`?)',
    f'<strong>Code repository:</strong> <a href="{github_url}" class="no-break-link" target="_blank">{github_url}</a>',
    body_html
)

# Convert any other raw urls to clickable links
body_html = re.sub(
    r'`(https://drive\.google\.com/[^`]+)`',
    r'<a href="\1" class="no-break-link" target="_blank">\1</a>',
    body_html
)

modern_css = """
@page {
    size: A4;
    margin: 14mm 14mm 16mm 14mm;
}

* {
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

/* Headings */
h1 {
    display: block !important;
    font-size: 22pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #0f2744 !important;
    margin-top: 0;
    margin-bottom: 14px;
    padding-bottom: 8px;
    border-bottom: 3px solid #2563eb;
    page-break-after: avoid;
    break-after: avoid;
}

h2 {
    display: block !important;
    font-size: 13.5pt;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #1e3a8a !important;
    margin-top: 24px;
    margin-bottom: 10px;
    padding: 6px 12px;
    background-color: #eff6ff;
    border-left: 5px solid #2563eb;
    border-radius: 0 4px 4px 0;
    page-break-after: avoid;
    break-after: avoid;
}

h3 {
    display: block !important;
    font-size: 11pt;
    font-weight: 700;
    color: #0284c7 !important;
    margin-top: 16px;
    margin-bottom: 6px;
    padding-bottom: 3px;
    border-bottom: 1px dashed #cbd5e1;
    page-break-after: avoid;
    break-after: avoid;
}

p {
    margin: 0 0 9px 0;
    color: #334155;
    text-align: justify;
}

/* Metadata Box */
h1 + p {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #2563eb;
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 9.5pt;
    line-height: 1.7;
    color: #334155;
    margin-bottom: 18px;
}

/* Clickable Links with no breaking */
a {
    color: #2563eb;
    text-decoration: underline;
    font-weight: 500;
}

.no-break-link {
    white-space: nowrap !important;
    display: inline-block;
    max-width: 100%;
    color: #1d4ed8;
    text-decoration: underline;
    font-family: Consolas, "Courier New", monospace;
    font-size: 8.5pt;
    vertical-align: middle;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9pt;
    page-break-inside: avoid;
    break-inside: avoid;
}

th {
    background: #1e293b;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 7px 10px;
    font-size: 8.5pt;
    border: 1px solid #1e293b;
}

td {
    padding: 6px 10px;
    border: 1px solid #e2e8f0;
    color: #334155;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

/* Code Blocks & Inline Code */
code {
    font-family: Consolas, "Courier New", monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
}

pre {
    background: #0f172a;
    color: #f8fafc;
    border-radius: 6px;
    padding: 10px 12px;
    margin: 10px 0;
    overflow-x: auto;
    font-family: Consolas, "Courier New", monospace;
    font-size: 8pt;
    line-height: 1.45;
    border-left: 4px solid #2563eb;
    page-break-inside: avoid;
    break-inside: avoid;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
}

/* Figure Cards */
.figure-card {
    margin: 14px 0;
    padding: 8px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
}

.figure-card img {
    display: block;
    margin: 0 auto;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
    max-width: 100%;
}

.figure-caption {
    margin-top: 6px;
    font-size: 8.5pt;
    color: #64748b;
}

.figure-caption span {
    font-weight: 700;
    color: #2563eb;
}

ul, ol {
    margin: 6px 0 10px 0;
    padding-left: 20px;
    color: #334155;
}

li {
    margin-bottom: 3px;
}
"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Heart Disease MLOps Report - Vishal Anand (2025AE05692)</title>
<style>
{modern_css}
</style>
</head>
<body>
{body_html}
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out}",
    html_path
]
subprocess.run(cmd, check=True)
print("Updated PDF with single-line clickable link generated successfully!")
