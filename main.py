from ocr_module import image_preprocessing, text_recognition

def main(image_path):
    # Image Preprocessing
    preprocessed_image = image_preprocessing.preprocess_image(image_path)

    # Text Recognition
    text = text_recognition.perform_ocr(preprocessed_image)
    
    print("Detected Text:")
    print(text)

if __name__ == "__main__":
    image_path = "sample_images/0.jpg"
    main(image_path)
