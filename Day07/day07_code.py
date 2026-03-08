from fpdf import FPDF

def generate_pdf(patient_name, patient_age, date, risk_level, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(0, 180, 216)
    pdf.cell(0, 15, "WoundAI - Medical Assessment Report", ln=True, align="C")
    # ... patient info, risk level, assessment, disclaimer
    return bytes(pdf.output())

st.download_button(
    label="📄 Download PDF Report",
    data=pdf_bytes,
    file_name=f"WoundAI_{patient_name}_{date}.pdf",
    mime="application/pdf"
)
