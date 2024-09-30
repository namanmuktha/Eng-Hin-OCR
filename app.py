import streamlit as st
from PIL import Image
import re
from ocr_model import OCRModel

# Function to extract text from the image using the OCRModel
def extract_text_from_image(image,loaded_model):
    # Extract text from the image using the loaded OCRModel
    extracted_text = loaded_model.process_image(image)
    return extracted_text

# Function to perform keyword search in extracted text
def search_keyword(text, keyword):
    if not text or not keyword:
        return text, []
    
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    # Highlight the search keyword with a yellow mark using inline CSS
    highlighted_text = pattern.sub(lambda m: f"<mark style='background-color: #fafa00;'>{m.group()}</mark>", text)
    
    matches = pattern.finditer(text)
    results = [m.start() for m in matches]
    
    return highlighted_text, results

# Load the OCR model once and cache it for future use
@st.cache_resource
def load_ocr_model():
    with st.spinner("Loading OCR model, please wait..."):
        return OCRModel()

# Web application setup using Streamlit
def main():
    st.title("OCR and Document Search Prototype")

    # Load the OCR model
    loaded_model = load_ocr_model()

    # Image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Load and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Extract text from the image
        st.write("Extracting text...")
        extracted_text = extract_text_from_image(image,loaded_model)
        st.write("Extracted Text:")
        st.write(extracted_text)

        # Keyword search functionality
        st.write("Search within the extracted text")
        keyword = st.text_input("Enter a keyword to search:")
        
        if keyword:
            highlighted_text, matches = search_keyword(extracted_text, keyword)
            if matches:
                st.write(f"Found {len(matches)} matches for '{keyword}':")
                st.markdown(highlighted_text, unsafe_allow_html=True)  # Display highlighted text
            else:
                st.write(f"No matches found for '{keyword}'")

if __name__ == "__main__":
    main()
