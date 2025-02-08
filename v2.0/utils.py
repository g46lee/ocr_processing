import os, datetime, cv2

def log_results(text, status, avg_confidence):
    """
    Logs flagged/invalid OCR results into a txt file with timestamp, text, confidence, and status details.
    """
    # Create "logs" directory/folder
    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_directory, "logs")
    os.makedirs(log_dir, exist_ok=True)

    # define txt file with current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_file_name = f"{current_date}.txt"
    log_file_path = os.path.join(log_dir, log_file_name)

    # time stamps with date and time for log entries
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log entry variations based on text validation in ocr_extraction.py
    # Case 1: No valid text detected
    if not text:
        log_entry = f"[{timestamp}] No valid text detected | Status: {status}\n"
    # Case 2: Text was extracted but contains non-digits or fails validation
    elif "Invalid" in status:
        log_entry = f"[{timestamp}] Extracted: {text} | Confidence: {avg_confidence:.2f}% | Status: {status}\n"
    # Case 3 : Valid text extraction
    else:
        log_entry = f"[{timestamp}] Digits: {text} | Confidence: {avg_confidence:.2f}% | Status: {status}\n"

    # Write/append the log entry to the log file
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)
    print(f"Log saved to: {log_file_path}") # Inform user the exact path at which logs were written at


def save_images(raw_image, processed_image, status):
    """
    Save raw and processed images for evaluation of failed OCR cases.
    """
    if status != "Valid":
        # Create failed_readings folder as well as subfolders according to the date
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        script_directory = os.path.dirname(os.path.abspath(__file__))
        failed_dir = os.path.join(script_directory, "failed_readings", current_date)

        # Create subfolders for "raw" and "processed" images
        raw_dir = os.path.join(failed_dir, "raw")
        processed_dir = os.path.join(failed_dir, "processed")
        os.makedirs(raw_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)

        # Save raw and processed images of failed OCR cases within their subfolders with date/time
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        raw_image_path = os.path.join(raw_dir, f"{timestamp}.jpg")
        processed_image_path = os.path.join(processed_dir, f"{timestamp}.jpg")
        cv2.imwrite(raw_image_path, raw_image)
        cv2.imwrite(processed_image_path, processed_image)

        return raw_image_path, processed_image_path
    return None, None