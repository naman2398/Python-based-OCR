import pytesseract
from PIL import Image
import cv2

def perform_ocr(image, lang='eng'):
    # Perform OCR using Tesseract with specified language
    custom_config = r'--oem 3 --psm 6 outputbase digits'  # Tesseract configuration options

    # Convert OpenCV image to PIL Image for compatibility with pytesseract
    pil_image = Image.fromarray(image)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(pil_image, lang=lang, config=custom_config)

    return text
