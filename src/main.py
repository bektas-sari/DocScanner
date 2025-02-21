import sys
import platform
from PyQt6.QtWidgets import QApplication
from gui import OCRApp
import pytesseract

# Set tesseract path for Windows; for Linux/Mac, assume tesseract is in PATH
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec())
