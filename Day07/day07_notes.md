## 📓 Day 07 — PDF Report Export
**Date:** March 8, 2026

### What I did:
- Installed `fpdf2` library for generating PDF files
- Built a `generate_pdf()` function that creates a professional report
- PDF includes patient name, age, assessment date, infection risk in color, full AI assessment and disclaimer
- Added a **Download PDF Report** button that instantly downloads the file
- File is named automatically using patient name and date

### What I learned:
- `pip install fpdf2` — library for creating PDF files in Python
- `FPDF()` — creates a new blank PDF document
- `pdf.add_page()` — adds a new page to the PDF
- `pdf.set_font("Helvetica", "B", 20)` — sets font, style (B=Bold, I=Italic), and size
- `pdf.set_text_color(r, g, b)` — sets text color using RGB values (0-255)
- `pdf.cell()` — adds a single line of text to the PDF
- `pdf.multi_cell()` — adds text that automatically wraps to next line
- `pdf.line()` — draws a horizontal line (used as divider)
- `pdf.output()` — converts finished PDF into bytes for downloading
- `st.download_button()` — creates a download button in Streamlit
- `mime="application/pdf"` — tells the browser this file is a PDF
- `.encode("latin-1", "replace")` — handles special characters that PDF can't display
- `bytes()` — converts PDF output into downloadable format

### Errors fixed:
- Special characters in AI response breaking PDF → used `.encode("latin-1", "replace")` to clean the text
