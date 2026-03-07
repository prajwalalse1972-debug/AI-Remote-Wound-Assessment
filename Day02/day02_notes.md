## 📓 Day 02 — Image Upload UI
**Date:** March 5, 2026

### What I did:
- Installed **Pillow** library using `pip install pillow`
- Added a **sidebar** with app description
- Added **patient name input** field
- Added **image file uploader** (JPG, JPEG, PNG)
- Image displays on screen after upload
- Success message shows after upload

### What I learned:
- `from PIL import Image` — loads image handling library
- `st.sidebar.title()` / `st.sidebar.write()` — creates a side panel
- `st.text_input()` — creates a text input box
- `st.file_uploader()` — creates drag and drop file upload
- `if uploaded_file is not None:` — only runs code if user uploaded something
- `Image.open()` — opens an image file
- `st.image()` — displays an image on the page
- `st.success()` — shows a green success message

### Errors I fixed:
- `app.py` kept saving inside `venv` folder → learned to always check breadcrumb path at top of VS Code
- Wrong terminal used → learned PowerShell with `(venv)` is the only correct terminal to use
- `.venv` vs `venv` confusion → two different virtual environments existed, always activate the correct one
