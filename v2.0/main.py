import cv2
from preprocessing import preprocess_image
from ocr_extraction import extract_text_with_confidence, validate_text_with_confidence
from utils import log_results, save_images
import pytesseract

# ROI box dimensions (width x height)
roi_width, roi_height = 300, 300

# Open the camera
cap = cv2.VideoCapture(0) # current default is ContinuityCamera
if not cap.isOpened():
    print("Error: Could not open webcam.") # debugging
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame. Retrying...") # debugging
        continue # instead of breaking (v1), continue to try grabbing frame 


    # 1st ROI:
    frame_height, frame_width = frame.shape[:2] # define frames and dimensions
    x = (frame_width - roi_width) // 2
    y = (frame_height - roi_height) // 2
    cv2.rectangle(frame, (x, y), (x + roi_width, y + roi_height), (0, 255, 0), 2) # Visualize the box
    roi = frame[y:y + roi_height, x:x + roi_width]
    thresh = preprocess_image(roi, 0, 0, roi_width, roi_height) # Preprocess the region
    ocr_data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)  # Perform OCR

    # 2nd ROI: more accurate ROI region within the 1st ROI box live-displays text and confidence information
    for i in range(len(ocr_data["text"])):
        text = ocr_data["text"][i].strip()
        conf = int(ocr_data["conf"][i])

        # Filter invalid or low-confidence results
        if text and conf > 85: # limit is set to 85%
            left = ocr_data["left"][i]
            top = ocr_data["top"][i]
            width = ocr_data["width"][i]
            height = ocr_data["height"][i]

            # Visualize the box
            cv2.rectangle(frame, (x + left, y + top), (x + left + width, y + top + height), (0, 255, 0), 2)

            # Overlay (visually) text and confidence values
            overlay_text = f"{text} ({conf}%)"
            cv2.putText(frame, overlay_text, (x + left, y + top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    # Display the live feed
    cv2.imshow("Live Camera Feed with Bounding Boxes", frame)


    # Manual capture of images
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # Spacebar for trigger
        
        # Validation and Logging
        extracted_text, avg_confidence = extract_text_with_confidence(thresh)
        status, cleaned_text = validate_text_with_confidence(extracted_text, avg_confidence)
        if status == "Valid":
            print(f"Valid Text Detected: {cleaned_text}")
            log_results(cleaned_text, status, avg_confidence)
        else:
            print(f"Validation Failed: {status}")
            log_results(extracted_text, status, avg_confidence)
            raw_path, processed_path = save_images(frame, thresh, status)
            print(f"Raw Image saved at: {raw_path}")
            print(f"Processed Image saved at: {processed_path}")
        break

    elif key == ord('q'):  # 'q' to exit
        cap.release()
        cv2.destroyAllWindows()
        exit()
cap.release()
cv2.destroyAllWindows() # end program
print("OCR & Validation Process Completed.")