## 📓 Day 01 — Project Setup & Hello World
**Date:** March 5, 2026

### What I did:
- Checked Python version (3.13.3) was installed
- Opened VS Code and used the built-in terminal (PowerShell)
- Created project folder `WoundAI` inside `Biobytes project`
- Created a **virtual environment** using `python -m venv venv`
- Fixed Windows security policy to allow scripts using `Set-ExecutionPolicy`
- Activated the virtual environment using `venv\Scripts\activate`
- Installed **Streamlit** using `pip install streamlit`
- Created `app.py` with 4 lines of code
- Successfully ran first web app at `localhost:8501`

### What I learned:
- What a **terminal** is and how to navigate folders using `cd`, `mkdir`, `dir`
- What a **virtual environment** is — a clean isolated space for project packages
- What **pip** is — Python's package installer
- `import streamlit as st` — loads a library and gives it a nickname
- `st.title()` — creates a heading on the webpage
- `st.write()` — displays text on the webpage
- **Hot reloading** — Streamlit auto-updates the browser when you save

### Errors I fixed:
- `cd desktop` failed → learned I was already inside a subfolder
- `venv\Scripts\activate` blocked → fixed Windows execution policy
- `streamlit not recognized` → learned to always use PowerShell with `(venv)` active
- `app.py not found` → learned files must be saved in the correct folder
