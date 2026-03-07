import groq, base64, io

if st.button("🔬 Analyse Wound"):
    with st.spinner("AI is analysing the wound..."):
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

        client = groq.Groq(api_key=st.secrets["GROQ_API_KEY"])
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[...]
        )
        st.write(response.choices[0].message.content)
