# Save to history
st.session_state.history.append({
    "patient": patient_name if patient_name else "Unknown",
    "date": datetime.datetime.now().strftime("%d %B %Y, %I:%M %p"),
    "risk": risk_level if 'risk_level' in dir() else "Unknown",
    "result": result
})

# Show history in sidebar
st.sidebar.markdown("---")
st.sidebar.title("📋 Past Assessments")

if len(st.session_state.history) == 0:
    st.sidebar.write("No assessments yet.")
else:
    for i, record in enumerate(reversed(st.session_state.history)):
        st.sidebar.markdown(f"""
        <div style="background:#1e1e2e; padding:10px; border-radius:8px; margin:5px 0;">
            <b>#{len(st.session_state.history) - i}</b> {record['patient']}<br>
            <small>{record['date']}</small><br>
            <small>Risk: {record['risk']}</small>
        </div>
        """, unsafe_allow_html=True)
