import cv2
import numpy as np
import os

def preprocess_image(image_path):
    # Load image
    original_image = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise and improve OCR accuracy
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Perform adaptive thresholding to emphasize text
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use morphological transformations to clean up the image
    kernel = np.ones((3, 3), np.uint8)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=2)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel, iterations=1)

    # Invert the image to have text in white
    inverted_image = cv2.bitwise_not(binary_image)

    # Apply edge detection using Canny
    edges = cv2.Canny(inverted_image, 30, 100)

    # Combine original image and edges using bitwise_or
    enhanced_image = cv2.bitwise_or(inverted_image, edges)

    # Apply contrast enhancement using histogram equalization
    enhanced_image = cv2.equalizeHist(enhanced_image)

    # Layout analysis to detect text regions
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Skew correction
    angle = get_skew_angle(enhanced_image)
    rotated_image = rotate_image(enhanced_image, angle)

    # Line removal using horizontal and vertical structuring elements
    removed_lines_image = remove_lines(rotated_image)

    pre_processed_image = removed_lines_image

    return pre_processed_image

def get_skew_angle(image):
    # Calculate skew angle using Hough Transform
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

    if lines is not None:
        angles = []
        for line in lines:
            _, angle = line[0]
            angles.append(angle)
        median_angle = np.median(angles)
        skew_angle = median_angle * 180 / np.pi
        return skew_angle
    else:
        return 0

def rotate_image(image, angle):
    # Rotate the image by the specified angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    return rotated_image

def remove_lines(image):
    # Remove horizontal lines
    horizontal_kernel = np.ones((1, 10), np.uint8)
    horizontal_lines = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
    image_no_horizontal_lines = image - horizontal_lines

    # Remove vertical lines
    vertical_kernel = np.ones((10, 1), np.uint8)
    vertical_lines = cv2.morphologyEx(image, cv2.MORPH_OPEN, vertical_kernel, iterations=1)
    image_no_lines = image_no_horizontal_lines - vertical_lines

    return image_no_lines
