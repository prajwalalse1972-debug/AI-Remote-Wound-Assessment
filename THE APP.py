import streamlit as st
from PIL import Image
import groq
import base64
import io
import datetime
import math
from fpdf import FPDF

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

# Risk detection function
def get_risk_level(text):
    text_lower = text.lower()
    if "high" in text_lower:
        return "High", "#ff4444", "🔴", 85
    elif "medium" in text_lower or "moderate" in text_lower:
        return "Medium", "#ffaa00", "🟡", 50
    else:
        return "Low", "#00cc44", "🟢", 15

# Risk meter function
def render_risk_meter(risk_level, risk_color, score):
    angle = -90 + (score / 100) * 180
    bg_color = risk_color + "22"
    needle_x = 80 + 50 * math.cos(math.radians(angle))
    needle_y = 90 + 50 * math.sin(math.radians(angle))
    dash = score * 1.885

    return f"""
    <div style="background:{bg_color}; border:2px solid {risk_color};
    border-radius:16px; padding:24px; display:flex;
    align-items:center; justify-content:space-between; margin:15px 0;">
        <div style="flex:1;">
            <p style="color:{risk_color}; font-size:0.75em; font-weight:700;
            letter-spacing:2px; text-transform:uppercase; margin:0;">
                INFECTION RISK LEVEL
            </p>
            <h1 style="color:{risk_color}; font-size:2.5em;
            font-weight:900; margin:8px 0;">{risk_level}</h1>
            <p style="color:#aaa; font-size:0.85em; margin:0;">
                AI-assessed infection probability
            </p>
        </div>
        <div style="flex:1; text-align:center;">
            <svg width="160" height="100" viewBox="0 0 160 100">
                <path d="M 20 90 A 60 60 0 0 1 140 90"
                    fill="none" stroke="#2a2a3e"
                    stroke-width="12" stroke-linecap="round"/>
                <path d="M 20 90 A 60 60 0 0 1 140 90"
                    fill="none" stroke="{risk_color}"
                    stroke-width="12" stroke-linecap="round"
                    stroke-dasharray="{dash} 188.5"
                    opacity="0.9"/>
                <line x1="80" y1="90"
                    x2="{needle_x}" y2="{needle_y}"
                    stroke="{risk_color}" stroke-width="3"
                    stroke-linecap="round"/>
                <circle cx="80" cy="90" r="6" fill="{risk_color}"/>
                <text x="80" y="75" text-anchor="middle"
                    fill="{risk_color}" font-size="18"
                    font-weight="bold">{score}</text>
            </svg>
            <p style="color:#888; font-size:0.7em; letter-spacing:2px;
            text-transform:uppercase; margin:0;">INFECTION RISK SCORE</p>
        </div>
    </div>
    """

# PDF generation function
def generate_pdf(patient_name, patient_age, date, risk_level, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(0, 180, 216)
    pdf.cell(0, 15, "WoundAI - Medical Assessment Report", ln=True, align="C")
    pdf.set_draw_color(0, 180, 216)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Patient Name: {patient_name if patient_name else 'Not provided'}", ln=True)
    pdf.cell(0, 10, f"Patient Age: {patient_age if patient_age else 'Not provided'}", ln=True)
    pdf.cell(0, 10, f"Assessment Date: {date}", ln=True)
    pdf.set_font("Helvetica", "B", 14)
    if risk_level == "High":
        pdf.set_text_color(255, 68, 68)
    elif risk_level == "Medium":
        pdf.set_text_color(255, 170, 0)
    else:
        pdf.set_text_color(0, 204, 68)
    pdf.cell(0, 12, f"Infection Risk: {risk_level}", ln=True)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Full Assessment:", ln=True)
    pdf.set_font("Helvetica", "", 10)
    clean_result = result.encode("latin-1", "replace").decode("latin-1")
    pdf.multi_cell(0, 7, clean_result)
    pdf.ln(5)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(128, 128, 128)
    pdf.multi_cell(0, 6, "DISCLAIMER: This is an AI-assisted assessment only. It does not replace professional medical advice.")
    return bytes(pdf.output())

# Custom CSS
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .app-header {
        background: linear-gradient(135deg, #0a0a0f 0%, #1e1e2e 100%);
        border-bottom: 2px solid #00b4d8;
        padding: 20px;
        margin: -60px -60px 30px -60px;
        text-align: center;
    }
    .app-header h1 { color: #00b4d8; font-size: 2.5em; margin: 0; letter-spacing: 2px; }
    .app-header p { color: #888; margin: 5px 0 0 0; font-size: 0.9em; letter-spacing: 1px; text-transform: uppercase; }
    .status-badge {
        display: inline-block;
        background: rgba(0, 180, 216, 0.1);
        border: 1px solid #00b4d8;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.75em;
        color: #00b4d8;
        margin-top: 8px;
    }
    .stButton > button {
        background: linear-gradient(135deg, #00b4d8, #0077b6);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 1.1em;
        font-weight: bold;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown("""
<div class="app-header">
    <h1>🩺 WoundAI</h1>
    <p>Remote Wound Assessment Platform</p>
    <span class="status-badge">● AI System Online</span>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("""
<div style="text-align:center; padding:10px 0;">
    <h2 style="color:#00b4d8;">🩺 WoundAI</h2>
    <p style="color:#888; font-size:0.8em;">REMOTE ASSESSMENT PLATFORM</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About")
st.sidebar.write("AI-powered wound assessment helping doctors remotely monitor infection risks using image analysis.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Session Stats")
col1, col2 = st.sidebar.columns(2)
col1.metric("Assessments", len(st.session_state.history))
col2.metric("High Risk", sum(1 for r in st.session_state.history if r['risk'] == 'High'))

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Past Assessments")
if len(st.session_state.history) == 0:
    st.sidebar.info("No assessments yet.")
else:
    for i, record in enumerate(reversed(st.session_state.history)):
        risk_colors = {"High": "#ff4444", "Medium": "#ffaa00", "Low": "#00cc44"}
        color = risk_colors.get(record['risk'], "#888")
        st.sidebar.markdown(f"""
        <div style="background:#1e1e2e; padding:10px; border-radius:8px;
        margin:5px 0; border-left:3px solid {color};">
            <b>#{len(st.session_state.history) - i}</b> {record['patient']}<br>
            <small style="color:#888;">{record['date']}</small><br>
            <small style="color:{color};">⬤ Risk: {record['risk']}</small>
        </div>
        """, unsafe_allow_html=True)

# Main content
st.markdown("### 👤 Patient Information")
col1, col2 = st.columns(2)
with col1:
    patient_name = st.text_input("Patient Name", placeholder="Enter patient full name")
with col2:
    patient_age = st.text_input("Patient Age", placeholder="Enter patient age")

st.markdown("### 📷 Wound Image")
uploaded_file = st.file_uploader("Upload a clear photo of the wound", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns([2, 1])
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Wound Image", width=500)
    with col2:
        st.markdown("""
        <div style="background:#1e1e2e; border-radius:12px; padding:20px; margin-top:10px;">
            <h4 style="color:#00b4d8;">📋 Tips for best results</h4>
            <p style="font-size:0.85em; color:#aaa;">
            ✓ Good lighting<br><br>
            ✓ Clear focus<br><br>
            ✓ Wound fully visible<br><br>
            ✓ Minimal background clutter
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.success("✅ Image uploaded successfully!")

    if st.button("🔬 Run AI Assessment"):
        with st.spinner("🤖 AI is analysing the wound image..."):

            buffer = io.BytesIO()
            image.save(buffer, format="JPEG")
            image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

            client = groq.Groq(api_key=st.secrets["GROQ_API_KEY"])
            response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}},
                        {"type": "text", "text": "You are a medical wound assessment AI. Analyse this wound image and provide: 1) Wound type, 2) Healing stage, 3) Infection risk (Low/Medium/High), 4) Key observations, 5) Recommendations for the doctor."}
                    ]
                }]
            )

            result = response.choices[0].message.content
            risk_level, risk_color, risk_emoji, risk_score = get_risk_level(result)

            st.session_state.history.append({
                "patient": patient_name if patient_name else "Unknown",
                "date": datetime.datetime.now().strftime("%d %B %Y, %I:%M %p"),
                "risk": risk_level,
                "result": result
            })

            # Patient report card
            st.markdown("---")
            st.markdown(f"""
            <div style="background:#1e1e2e; padding:20px; border-radius:12px; border-left:5px solid #00b4d8;">
                <h3 style="color:#00b4d8; margin:0 0 15px 0;">📋 Patient Report</h3>
                <table style="width:100%; color:#fff;">
                    <tr><td style="color:#888; width:40%; padding:6px 0;">Patient Name</td><td><b>{patient_name if patient_name else "Not provided"}</b></td></tr>
                    <tr><td style="color:#888; padding:6px 0;">Age</td><td><b>{patient_age if patient_age else "Not provided"}</b></td></tr>
                    <tr><td style="color:#888; padding:6px 0;">Assessment Date</td><td><b>{datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")}</b></td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

            # Risk meter
            st.markdown(render_risk_meter(risk_level, risk_color, risk_score), unsafe_allow_html=True)

            # Full assessment
            st.markdown("### 📝 Full Assessment")
            st.write(result)

            # PDF download
            current_date = datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")
            pdf_bytes = generate_pdf(patient_name, patient_age, current_date, risk_level, result)
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_bytes,
                file_name=f"WoundAI_{patient_name}_{datetime.datetime.now().strftime('%d%m%Y')}.pdf",
                mime="application/pdf"
            )

            st.markdown("---")
            st.warning("⚠️ This is an AI-assisted assessment. Always consult a qualified medical professional.")
