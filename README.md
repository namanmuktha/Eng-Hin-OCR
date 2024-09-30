# OCR and Keyword Search Web Application

This project is a web application built using Streamlit that allows users to upload images, extract text using an OCR model, and perform keyword searches within the extracted text.

## Features

- Upload images and extract text using an OCR model.
- Perform keyword searches within the extracted text.
- Highlight keywords in the extracted text.

## Installation

1. **Clone the repository**:
    ```sh
    git clone hhttps://github.com/Vignesh1625/Hindi-English-OCR
    cd Hindi-English-OCR
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Load the OCR model**:
    Ensure that the OCR model is available and properly configured in the [`ocr_model.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FWork%2FOCR%2Focr_model.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22cc50ae44-9ab4-4710-9454-b8fadf6b8039%22%5D "ocr_model.py") file.

2. **Run the application**:
    ```sh
    streamlit run app.py
    ```

3. **Open your browser**:
    Navigate to `http://localhost:8501` to use the application.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.