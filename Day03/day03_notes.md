## 📓 Day 03 — AI Integration
**Date:** March 6, 2026

### What I did:
- Got a free **Groq API key** from console.groq.com
- Created `.streamlit/secrets.toml` to store API key safely
- Installed `groq` library using `pip install groq`
- Connected the app to **Llama 4 Scout** vision AI model
- Added **Analyse Wound** button
- App now sends image to AI and gets real medical assessment back
- Used `base64` encoding to convert image for sending over internet

### What I learned:
- **API key** — a secret password to access an AI service
- `secrets.toml` — safe place to store API keys, never put them in code
- `base64` — converts binary image data into text so it can be sent over internet
- `io.BytesIO()` — temporary memory buffer to hold image data
- `groq.Groq()` — creates connection to Groq AI service
- `client.messages.create()` — sends request to AI
- `st.button()` — creates a clickable button
- `st.spinner()` — shows loading animation while AI is thinking
- **Indentation in Python** — spaces matter! Code inside `if`/`with` must be indented

### Errors I fixed:
- Claude API too expensive → switched to Groq (free)
- Gemini quota exceeded → switched to Groq
- Multiple wrong model names → found working `meta-llama/llama-4-scout-17b-16e-instruct`
- `secrets.toml` in wrong folder → must be at `WoundAI/.streamlit/secrets.toml`
- Accidentally shared API key in screenshot → immediately regenerated key
