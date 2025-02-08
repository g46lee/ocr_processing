import cv2
from preprocessing import preprocess_image
from ocr_extraction import extract_text, validate_text
from utils import log_results, save_images

# ROI box dimensions (width x height)
roi_width, roi_height = 300, 100

# Capture image via Manual Trigger using webcam
cap = cv2.VideoCapture(0) # current default is ContinuityCamera
if not cap.isOpened():
    print("Error: Could not open webcam.") # debugging
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.") # debugging
        break

    # Frame dimensions and center for ROI
    frame_height, frame_width = frame.shape[:2]
    x = (frame_width - roi_width) // 2
    y = (frame_height - roi_height) // 2
    # Visualize the ROI box in the center of the screen
    cv2.rectangle(frame, (x, y), (x + roi_width, y + roi_height), (0, 255, 0), 2)
    cv2.imshow("Live Camera Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # Spacebar as trigger
        captured_frame = frame.copy()  # Save the captured frame
        break
    elif key == ord('q'):  # 'q' to exit camera window
        cap.release()
        cv2.destroyAllWindows()
        exit()
cap.release()
cv2.destroyAllWindows()


thresh = preprocess_image(captured_frame, x, y, roi_width, roi_height) # Preprocess captured image
text = extract_text(thresh) # Perform OCR
status, numbers = validate_text(text) # Validate extracted text
log_results(numbers, status) # Log extracted text as well as validation status(es)

# Save raw and processed images of flagged items for evaluation
if status != "Valid":
    raw_path, processed_path = save_images(captured_frame, thresh, status)
    # Update User about the progress
    print(f"Error: {status}")
    print(f"Raw Image saved at: {raw_path}")
    print(f"Processed Image saved at: {processed_path}")
else:
    print(f"Valid Text Extracted: {numbers}")
print("OCR Process Completed.")