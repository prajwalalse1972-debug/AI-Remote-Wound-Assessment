def get_risk_level(text):
    text_lower = text.lower()
    if "high" in text_lower:
        return "High", "#ff4444", "🔴"
    elif "medium" in text_lower or "moderate" in text_lower:
        return "Medium", "#ffaa00", "🟡"
    else:
        return "Low", "#00cc44", "🟢"

# Detect and show risk level
risk_level, risk_color, risk_emoji = get_risk_level(result)

st.markdown(f"""
<div style="
    background-color: {risk_color}22;
    border: 2px solid {risk_color};
    border-radius: 10px;
    padding: 16px;
    text-align: center;
    margin: 10px 0;
">
    <h2 style="color: {risk_color}; margin: 0;">
        {risk_emoji} Infection Risk: {risk_level}
    </h2>
</div>
""", unsafe_allow_html=True)
