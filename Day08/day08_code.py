import math

def get_risk_level(text):
    # Now returns 4 values including score
    if "high" in text_lower:
        return "High", "#ff4444", "🔴", 85
    elif "medium" in text_lower:
        return "Medium", "#ffaa00", "🟡", 50
    else:
        return "Low", "#00cc44", "🟢", 15

def render_risk_meter(risk_level, risk_color, score):
    angle = -90 + (score / 100) * 180
    needle_x = 80 + 50 * math.cos(math.radians(angle))
    needle_y = 90 + 50 * math.sin(math.radians(angle))
    # Returns HTML with SVG gauge meter

# config.toml
[theme]
primaryColor = "#00b4d8"
backgroundColor = "#0a0a0f"
secondaryBackgroundColor = "#1e1e2e"
textColor = "#ffffff"
