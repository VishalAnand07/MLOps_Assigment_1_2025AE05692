import os
import re
import markdown
import subprocess

report_dir = r"C:\Users\visha\Downloads\New folder (2)\mlops-assign\report"
md_path = os.path.join(report_dir, "REPORT.md")
css_path = os.path.join(report_dir, "report.css")
html_path = os.path.join(report_dir, "REPORT.html")
pdf_path = os.path.join(report_dir, "REPORT.pdf")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

def clean_img(m):
    alt = m.group(1)
    src = m.group(2)
    w = m.group(3)
    # src is like ../screenshots/01_mlflow_... or architecture.png
    return f'<figure style="text-align:center; margin:14px 0;"><img src="{src}" style="width:{w}%; max-width:100%; border:1px solid #ddd; border-radius:4px;" alt="{alt}"/><figcaption style="font-size:9pt; color:#555; font-style:italic; margin-top:4px;">{alt}</figcaption></figure>'

text = re.sub(r"!\[(.*?)\]\((.*?)\)\{width=(\d+)%\}", clean_img, text)

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

body_html = markdown.markdown(text, extensions=["tables", "fenced_code"])

full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Heart Disease MLOps Report - Vishal Anand (2025AE05692)</title>
<style>
{css}
@page {{
    size: A4;
    margin: 12mm 12mm 12mm 12mm;
}}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}}
figure {{
    page-break-inside: avoid;
    break-inside: avoid;
}}
pre, table {{
    page-break-inside: avoid;
    break-inside: avoid;
}}
</style>
</head>
<body>
{body_html}
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML generated successfully at:", html_path)

# Convert HTML to PDF using Chrome or Edge headless
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
browser = chrome_path if os.path.exists(chrome_path) else edge_path

cmd = [
    browser,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("PDF printed successfully to:", pdf_path)
