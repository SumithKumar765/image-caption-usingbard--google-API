import streamlit as st
import httpx
import base64
import google.generativeai as genai
import user_config

# Configure API key
genai.configure(api_key=user_config.openai_key)

# Initialize GenerativeModel
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Function to generate image caption
def generate_caption(image_file):
    # Read image file
    image = image_file.read()
    # Encode image to base64
    encoded_image = base64.b64encode(image).decode('utf-8')
    # Prompt for image caption
    prompt = "Caption this image."
    # Generate content
    response = model.generate_content([{'mime_type': 'image/jpeg', 'data': encoded_image}, prompt])
    return response.text

# Streamlit app
def main():
    st.title("Image Caption Generator --> \n Author sumith")
    st.markdown("Upload an image and generate a caption.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        # Generate caption on button click
        if st.button('Generate Caption'):
            with st.spinner('Generating caption...'):
                caption = generate_caption(uploaded_file)
            st.success('Caption generated:')
            st.write(caption)

if __name__ == '__main__':
    main()
