import os
import platform
import pytesseract

def ensure_tesseract_path():
    """
    Ensure Tesseract is configured correctly based on the operating system.
    For Windows, checks if the Tesseract executable exists at the default path and sets it.
    For Linux and Mac, assumes Tesseract is installed and available in PATH.
    """
    system = platform.system()
    if system == "Windows":
        tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        if os.path.exists(tesseract_path):
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        else:
            print("Warning: Tesseract not found in the default Windows path. Please install or update the path accordingly.")
    else:
        # For Linux and Mac, we assume Tesseract is installed and in the PATH.
        pass
