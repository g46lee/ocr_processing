# OCR System for Real-Time Text Recognition  
This repository contains the source code for a real-time Optical Character Recognition (OCR) system developed using Python, OpenCV, and Tesseract.  
The project has been developed over versions, each iteration built upon the previous version.

- **Version 1.0 (2023):** Established the core OCR pipeline with manual frame capture and basic preprocessing.  
- **Version 2.0 (2024):** Introduced real-time OCR visualization, improved preprocessing, and stricter validation logic.  
- **Version 3.0 (Expected 2025):** Will integrate a **Graphical User Interface (GUI)** for enhanced usability and interactivity.  

---

## Version Overview

### **Version 1.0 (2023)**
Implemented the OCR pipeline for capturing and validating text in a predefined ROI using a webcam.

**Key Features:**
- **Tesseract OCR Integration:** Extracted text from a fixed Region of Interest (ROI) using Tesseract OCR.
- **Manual Triggering:** Allowed users to manually capture frames via a spacebar trigger.
- **Preprocessing Pipeline:** Included grayscale conversion, Gaussian blur, and adaptive thresholding for text segmentation.
- **Validation Logic:** Validated extracted text to ensure:
  - It contained at least six digits.
  - Only numeric characters were retained.
- **Result Logging and Debugging:**
  - Logged extracted text and validation results into `ocr_results.txt`.
  - Saved raw and preprocessed images of failed cases to a structured folder.

**Limitations:**
- Required manual interaction for text alignment and triggering.
- Relied on a static ROI, limiting adaptability for varying text placements.
- No real-time OCR visualization or live feedback.

---

### **Version 2.0 (2024)**
Introduced dynamic features for real-time OCR visualization and enhanced feedback.

**Key Features:**
- **Real-Time OCR Visualization:**
  - Live OCR processing with results overlaid directly on the camera feed.
  - Confidence scores displayed alongside extracted text.
- **Dynamic Bounding Boxes:**
  - Identified text regions within the ROI using bounding boxes drawn dynamically based on OCR outputs.
- **Preprocessing Enhancements:**
  - Added noise normalization, sharpening, and morphological operations for better text extraction.
- **Expanded Validation:**
  - Incorporated confidence thresholds to reject low-confidence results.
  - Improved validation logic for ensuring exactly six numeric digits.
- **Improved Logging and Organization:**
  - Automatically organized logs and images into date-specific folders for better traceability.
  - Separated failed cases into "raw" and "processed" subfolders.

**Benefits of Version 2.0:**
- Allows visual access to OCR results live.
- Enhanced feedback with bounding boxes and confidence-based insights.
- Improved adaptability to various text quality and environmental conditions.

---

## Results
- **Accuracy Achieved**:  
  - v1.0: ~70% accuracy on simple, high-contrast text.
  - v2.0: ~90%+ accuracy due to advanced preprocessing and validation.
- **Performance Improvements**:  
  - Real-time visualization in v2.0 enhanced usability and confidence in the system.
  - Noise reduction and thresholding in preprocessing reduced OCR errors significantly.


## Version 3.0 (Upcoming, 2025) 
Version 3.0 will introduce a **Graphical User Interface (GUI)** to improve usability and streamline real-time OCR operations. Built with **PyQt6**, this version will enhance interactivity while maintaining the core functionality of previous versions.

**Key Enhancements:**  
- **Graphical Interface for OCR Operations:**  
  - Live camera feed displayed within a dedicated GUI window with an adjustable ROI box.  
  - Interactive buttons for triggering OCR, starting/stopping the feed, and saving results.  

- **Improved Real-Time Feedback:**  
  - Live OCR output with confidence scores displayed directly in the GUI.  
  - Enhanced visualization of detected text, reducing the need for external debugging.  

## Repository Structure
```plaintext
.
├── Version1.0/
│   ├── main.py
│   ├── preprocessing.py
│   ├── ocr_extraction.py
│   ├── utils.py
│   └── logs/
├── Version2.0/
│   ├── main.py
│   ├── preprocessing.py
│   ├── ocr_extraction.py
│   ├── utils.py
│   └── logs/
└── README.md
