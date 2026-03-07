import datetime

st.markdown(f"""

    📋 Patient Report
    Patient Name: {patient_name}
    Date: {datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")}

""", unsafe_allow_html=True)

st.warning("⚠️ This is an AI-assisted assessment...")
