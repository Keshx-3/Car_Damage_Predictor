import streamlit as st
from model_helper import predict
from PIL import Image

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Open the image using Pillow
    img = Image.open(image_path)
    
    # Resize the image
    img = img.resize((300, 300))
    
    # Save the resized image
    img.save(image_path)

    # Display the resized image
    st.image(image_path, caption="Uploaded File", use_container_width=True)
    
    # Get prediction
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
