import pytesseract, re

def extract_text(image):
    """Extract text using Tesseract OCR."""
    text = pytesseract.image_to_string(image)
    return text

def validate_text(text):
    """Validate that the text contains at least 6 digits."""
    numbers = ''.join(re.findall(r'\d+', text)).strip()
    if numbers.isdigit() and len(numbers) >= 6:
        return "Valid", numbers
    else:
        return "Incomplete Text Detected", numbers