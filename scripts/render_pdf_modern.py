import os
import re
import markdown
import subprocess

report_dir = r"C:\Users\visha\Downloads\New folder (2)\mlops-assign\report"
md_path = os.path.join(report_dir, "REPORT.md")
html_path = os.path.join(report_dir, "REPORT.html")
pdf_out = os.path.join(report_dir, "REPORT_FINAL.pdf")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace images with premium card styling
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

# Convert markdown tables & code
body_html = markdown.markdown(text, extensions=["tables", "fenced_code"])

# Premium Academic & Modern MLOps Engineering Template
modern_css = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

@page {
    size: A4;
    margin: 16mm 16mm 18mm 16mm;
    @bottom-center {
        content: counter(page);
    }
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

/* Document Title (H1) */
h1 {
    font-size: 24pt;
    font-weight: 800;
    letter-spacing: -0.025em;
    color: #0f172a;
    background: linear-gradient(135deg, #0f172a 0%, #1e40af 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 0;
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e2e8f0;
}

/* Section Headings (H2) */
h2 {
    font-size: 14pt;
    font-weight: 700;
    letter-spacing: -0.015em;
    color: #1e3a8a;
    margin-top: 26px;
    margin-bottom: 10px;
    padding: 6px 14px;
    background: linear-gradient(90deg, #eff6ff 0%, #f8fafc 100%);
    border-left: 5px solid #2563eb;
    border-radius: 0 6px 6px 0;
    page-break-after: avoid;
    break-after: avoid;
}

/* Subsection Headings (H3) */
h3 {
    font-size: 11.5pt;
    font-weight: 600;
    color: #0369a1;
    margin-top: 18px;
    margin-bottom: 8px;
    padding-bottom: 4px;
    border-bottom: 1px dashed #cbd5e1;
    page-break-after: avoid;
    break-after: avoid;
}

p {
    margin: 0 0 10px 0;
    color: #334155;
    text-align: justify;
}

/* Student & Meta Header Information Box */
h1 + p {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #3b82f6;
    padding: 12px 16px;
    border-radius: 6px;
    font-size: 9.5pt;
    line-height: 1.6;
    color: #334155;
    margin-bottom: 22px;
}

h1 + p strong {
    color: #0f172a;
}

/* Tables */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 14px 0;
    font-size: 9pt;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
    page-break-inside: avoid;
    break-inside: avoid;
}

th {
    background: #1e293b;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 9px 12px;
    letter-spacing: 0.02em;
    font-size: 8.5pt;
    text-transform: uppercase;
}

td {
    padding: 8px 12px;
    border-bottom: 1px solid #f1f5f9;
    color: #334155;
}

tr:last-child td {
    border-bottom: none;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

/* Code Blocks & Inline Code */
code {
    font-family: 'JetBrains Mono', Consolas, Menlo, monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}

pre {
    background: #0f172a;
    color: #f8fafc;
    border-radius: 8px;
    padding: 12px 14px;
    margin: 12px 0;
    overflow-x: auto;
    font-family: 'JetBrains Mono', Consolas, Menlo, monospace;
    font-size: 8pt;
    line-height: 1.5;
    border: 1px solid #1e293b;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
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

/* Figure / Screenshot Cards */
.figure-card {
    margin: 18px 0;
    padding: 10px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    box-shadow: 0 4px 10px -2px rgba(0, 0, 0, 0.04);
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
}

.figure-card img {
    display: block;
    margin: 0 auto;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    max-width: 100%;
}

.figure-caption {
    margin-top: 8px;
    font-size: 8.5pt;
    color: #64748b;
    font-style: normal;
}

.figure-caption span {
    font-weight: 700;
    color: #2563eb;
}

ul, ol {
    margin: 6px 0 12px 0;
    padding-left: 22px;
    color: #334155;
}

li {
    margin-bottom: 4px;
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
print("Updated HTML with new premium styles created!")

# Convert to PDF
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
print("Updated REPORT_FINAL.pdf generated successfully!")
