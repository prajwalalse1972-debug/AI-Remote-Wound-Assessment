from PIL import Image

st.sidebar.title("About")
st.sidebar.write("This app uses AI to assess wound images...")

patient_name = st.text_input("Enter Patient Name:")
if patient_name:
    st.write("Patient:", patient_name)

uploaded_file = st.file_uploader("Upload Wound Image", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Wound Image", width=600)
    st.success("Image uploaded successfully!")
