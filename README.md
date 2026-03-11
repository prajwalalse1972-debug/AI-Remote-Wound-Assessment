# 🩺 WoundAI - Remote Wound Assessment

A smartphone-based AI web app that assesses wound healing using image analysis, 
helping doctors remotely monitor infection risks.

Built for **Biobytes Hackathon 2026** 🏆

---

## 🚀 What it does
- Upload a wound image from any device
- AI analyses the wound instantly
- Provides detailed clinical assessment including:
  - Wound type identification
  - Healing stage detection
  - Infection risk level (Low/Medium/High)
  - Key clinical observations
  - Recommendations for the doctor
- Generates a timestamped patient report

---

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.13 | Core programming language |
| Streamlit | Web app framework |
| Groq API | Free AI inference platform |
| Llama 4 Scout | Vision AI model for image analysis |
| Pillow | Image processing |

---

## 📁 Project Structure
```
WoundAI/
├── .streamlit/
│   └── secrets.toml    ← API keys (not uploaded to GitHub)
├── venv/               ← Virtual environment (not uploaded)
├── app.py              ← Main application
├── .gitignore          ← Ignores secrets and venv
└── README.md           ← This file
```

---

## ⚙️ How to run locally
```bash
# 1. Clone the repo
git clone https://github.com/yourusername/WoundAI.git
cd WoundAI

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install streamlit pillow groq

# 4. Add your API key
# Create .streamlit/secrets.toml and add:
# GROQ_API_KEY = "your-key-here"

# 5. Run the app
streamlit run app.py
```

---

## 🔑 Getting API Keys
- **Groq API** (Free): https://console.groq.com

---

## 📅 Development Log
| Day | What was built |
|-----|---------------|
| Day 1 | Project setup, virtual environment, Hello World app |
| Day 2 | Image upload UI, patient name input, sidebar |
| Day 3 | Groq AI integration, real wound analysis working |
| Day 4 | Professional report UI, timestamps, medical disclaimer |
| Day 5 | Infection risk color indicator  |
| Day 6 | Patient history tracking  |
| Day 7 | PDF report export  |

---

## ⚠️ Disclaimer
This app is for educational and assistive purposes only. 
It does not replace professional medical advice or diagnosis.

git remote add origin https://github.com/yourusername/WoundAI.git
git branch -M main
git push -u origin main
