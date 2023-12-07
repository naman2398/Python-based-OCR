import pytesseract
from PIL import Image
import cv2

def perform_ocr(image):
    
    # Convert OpenCV image to PIL Image for compatibility with pytesseract
    pil_image = Image.fromarray(image)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(pil_image)

    return text
