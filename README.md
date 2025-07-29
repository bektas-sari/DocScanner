# DocScanner OCR Application

DocScanner is a modern, user-friendly, and scalable desktop OCR application built with Python, PyQt6, and Tesseract OCR.

## Features

- **Image Upload:** Easily upload images to extract text.
- **Multi-language Support:** OCR in multiple languages (English and Turkish).
- **Real-time Processing:** Utilizes threading for improved performance.
- **Text Editing:** Edit, copy, and save extracted text as TXT or PDF.
- **Cross-Platform:** Works on Windows, Linux, and macOS.

## Installation

### Clone the Repository:
```bash
git clone https://github.com/bektas-sari/DocScanner.git
cd DocScanner
```

### Create a Virtual Environment:
```bash
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Install Requirements:
```bash
pip install -r requirements.txt
```

### Configure Tesseract:
- **For Windows:** Ensure Tesseract is installed in `C:\Program Files\Tesseract-OCR\tesseract.exe`.
- **For Linux/Mac:** Ensure Tesseract is installed and accessible via PATH.

## Usage

Run the application:
```bash
python main.py
```

## Testing

Run unit tests:
```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License.


## 👤 Developer

**Bektas Sari**  
Email: bektas.sari@gmail.com  <br>
GitHub: https://github.com/bektas-sari <br>
LinkedIn: www.linkedin.com/in/bektas-sari <br>
Researchgate: https://www.researchgate.net/profile/Bektas-Sari-3 <br>
Academia: https://independent.academia.edu/bektassari <br>
