import cv2
import numpy as np

def preprocess_image(image, x, y, w, h):
    """Enhanced preprocessing with noise reduction, sharpening, and robust thresholding."""
    roi = image[y:y + h, x:x + w]
    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) # convert to grayscale
    gray_normalized = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX) # normalize brightness
    blurred = cv2.GaussianBlur(gray_normalized, (5, 5), 0) # Gaussian Blur
    _, otsu_thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Otsu's thresholding

    # Perform morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph_cleaned = cv2.morphologyEx(otsu_thresh, cv2.MORPH_CLOSE, kernel)

    return morph_cleaned