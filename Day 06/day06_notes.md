## 📓 Day 06 — Patient History Tracking
**Date:** March 8, 2026

### What I did:
- Added session state to remember past assessments
- Each analysis saves patient name, date, risk level
- Sidebar shows all past assessments with timestamps
- Newest assessment always appears at the top

### What I learned:
- `st.session_state` — Streamlit's memory during a session
- `if "key" not in st.session_state` — safely initialise state
- `list.append()` — adds items to a list
- `{}` dictionary — stores data as key/value pairs
- `enumerate()` — loop with a counter
- `reversed()` — shows newest items first
- Streamlit reruns top to bottom on every interaction
