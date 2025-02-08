import pytesseract, re

# Minimum confidence threshold for valid OCR
CONFIDENCE_THRESHOLD = 85

def extract_text_with_confidence(image):
    """
    Perform OCR on the given image, extract text and confidence scores.
    """
    ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DATAFRAME) # Perform OCR with detailed output
    ocr_data = ocr_data.dropna(subset=['text']) # Drop rows with missing values in 'text'
    ocr_data['text'] = ocr_data['text'].astype(str) # treat 'text' column as str

    # Extract text and confidence
    extracted_text = " ".join(ocr_data['text'])
    confidence_scores = ocr_data['conf']
    print(f"DEBUG: Raw OCR Output: {extracted_text}") # debugging, obtain raw OCR Output prior to validation
    avg_confidence = confidence_scores.mean() # Calculate avg confidence

    return extracted_text, avg_confidence


def validate_text_with_confidence(text, confidence):
    """
    Validate the extracted text based on:
    - Confidence threshold (currently 85%)
    - Text containing exactly 6 digits
    """
    cleaned_text = ''.join(re.findall(r'\d+', text)).strip() # only extract digits
    print(f"Cleaned Extracted Digits: {cleaned_text}") # debugging, obtain extracted digits prior to validation

    # Conditions for 'invalid' cases
    # Condition 1: cleaned_text is empty (no digits found)
    if not cleaned_text:
        return "Invalid: No digits detected in OCR output", cleaned_text
    # Condition 2: cleaned_text is not 6 digits (more or less than 6)
    if len(cleaned_text) != 6:
        return f"Invalid: Incorrect digit count (expected 6, got {len(cleaned_text)})", cleaned_text # debugging: mention actual length
    # Condition 3: confidence threshold to attain cleaned_text is lesser than threshold
    if confidence < CONFIDENCE_THRESHOLD:
        return f"Invalid: Low confidence ({confidence:.2f}%)", cleaned_text # debugging: mention actual confidence value

    return "Valid", cleaned_text
