import pytesseract
from PIL import Image
from utils import ensure_tesseract_path

def extract_text(image_path, language='eng'):
    """
    Extract text from an image using Tesseract OCR.

    :param image_path: Path to the image file
    :param language: Language code for OCR (default is English)
    :return: Extracted text as string
    """
    ensure_tesseract_path()
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=language)
        return text
    except Exception as e:
        return f"Error processing image: {str(e)}"
