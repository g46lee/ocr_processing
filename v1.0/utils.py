import os, datetime, cv2

def log_results(text, status):
    """Log OCR results as well as validation status to a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ocr_results.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] Extracted Text: {text} | Status: {status}\n")

def save_images(raw_image, processed_image, status):
    """Save raw and processed images for evaluation of failed OCR cases"""
    if status != "Valid":
        os.makedirs("failed_readings/processed_images", exist_ok=True)
        base_filename = f"error_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        raw_image_path = os.path.join("failed_readings", f"{base_filename}.jpg")
        processed_image_path = os.path.join("failed_readings/processed_images", f"{base_filename}.jpg")
        cv2.imwrite(raw_image_path, raw_image)
        cv2.imwrite(processed_image_path, processed_image)
        return raw_image_path, processed_image_path
    return None, None