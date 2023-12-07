# OCR Project with OpenCV and Tesseract

## Overview

This OCR (Optical Character Recognition) project utilizes OpenCV for image preprocessing and Tesseract for text recognition. OCR is a technology that extracts text from images, making it possible to convert scanned documents, images, or handwritten text into machine-readable text.

### Applications of OCR

- **Document Digitization:** OCR allows for the conversion of physical documents into digital formats, making them searchable and editable.
  
- **Text Extraction from Images:** Extracting text content from images, such as photographs, screenshots, or scanned pages.
  
- **Data Entry Automation:** Automate data entry tasks by extracting text information from documents or forms.
  
- **Document Classification:** Classify documents based on their content by analyzing extracted text.
  
- **Accessibility:** Improve accessibility by converting text from images into readable text for visually impaired individuals.

## Preprocessing Steps

### 1. Grayscale Conversion

The original image is converted to grayscale using OpenCV. This simplifies the image and reduces the number of channels.

### 2. Gaussian Blur

Gaussian blur is applied to the grayscale image to reduce noise and create a smoother image, enhancing OCR accuracy.

### 3. Adaptive Thresholding

Adaptive thresholding is used to segment the image into foreground (text) and background. It adapts to varying lighting conditions.

### 4. Morphological Transformations

Morphological operations, such as closing and opening, are applied to clean up the image by removing small noise and filling gaps.

### 5. Inversion

The image is inverted to have white text on a black background. This inversion is often beneficial for better compatibility with OCR engines.

### 6. Edge Detection (Canny)

Canny edge detection is employed to highlight edges in the image, improving text segmentation.

### 7. Histogram Equalization

Histogram equalization is applied to enhance the contrast of the image, making the text stand out.

### 8. Layout Analysis and Skew Correction

Contour detection is used to perform layout analysis and identify text regions. Skew correction is applied to correct any rotational skew in the document.

### 9. Line Removal

Horizontal and vertical lines are removed using morphological operations, eliminating interference from grid lines or table borders in documents.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/namam2398/ocr-project.git

2. **Install Dependencies:**
  ```bash
   pip install -r requirements.txt
   ```
3. **Run the OCR:**
  ```bash
   python main.py
  ```
## Customizations

- **Modify Preprocessing Steps:** Adjust the preprocessing steps in `ocr_module/image_preprocessing.py` to suit your document characteristics.
  
- **Fine-Tune OCR Parameters:** Experiment with Tesseract configuration options in `ocr_module/text_recognition.py` for optimal text recognition.
  
- **Handle Different Languages:** Set the language parameter in `main.py` and `ocr_module/text_recognition.py` for multilingual support.

Feel free to extend and adapt this project based on your specific use cases and requirements. Contributions and improvements are welcome!

---

This README now includes a brief explanation of each preprocessing step used in the OCR project, providing a clearer understanding of the image processing pipeline. 

