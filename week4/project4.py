# ============================================================
# PROJECT 4 - OCR Text Recognition
# DecodeLabs AI Engineer Training Kit
# ============================================================

# --- STEP 1: IMPORTS ---
import cv2
import pytesseract
from PIL import Image
import numpy as np
import os
import sys

# Auto-detect Tesseract on ANY machine (Windows / Mac / Linux)


def find_tesseract():
    possible_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        r'C:\Users\{}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'.format(
            os.getenv('USERNAME', '')),
        r'/usr/bin/tesseract',
        r'/usr/local/bin/tesseract',
    ]

    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            print("Tesseract found at: " + path)
            return True

    # Try system PATH as fallback
    import shutil
    if shutil.which('tesseract'):
        print("Tesseract found in system PATH")
        return True

    # Not found - give clear instructions
    print("ERROR: Tesseract not found!")
    print("   Install it from: https://github.com/UB-Mannheim/tesseract/wiki")
    sys.exit(1)


find_tesseract()
print("Step 1 Done: Libraries loaded successfully!")

# --- STEP 2: CREATE TEST IMAGE ---
img = np.ones((300, 600, 3), dtype=np.uint8) * 255

cv2.putText(img, "Invoice #0042",    (50, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
cv2.putText(img, "Date: 2024-01-15", (50, 140),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
cv2.putText(img, "Total: $499.00",   (50, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
cv2.putText(img, "Status: PAID",     (50, 260),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

cv2.imwrite("test_image.jpg", img)
print("Step 2 Done: Test image created!")

# --- STEP 3: PRE-PROCESSING ---

# 3a. Grayscale - remove color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Step 3a Done: Grayscale conversion")

# 3b. Gaussian Blur - smooth out noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)
print("Step 3b Done: Gaussian blur applied")

# 3c. Thresholding - force pixels to pure black or white
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
print("Step 3c Done: Thresholding applied")

cv2.imwrite("preprocessed_image.jpg", thresh)
print("Preprocessed image saved!")

# --- STEP 4: RUN OCR + CONFIDENCE SCORES ---
pil_image = Image.fromarray(thresh)
data = pytesseract.image_to_data(
    pil_image, output_type=pytesseract.Output.DICT)

print("\n" + "="*50)
print("        OCR RESULTS WITH CONFIDENCE")
print("="*50)

valid_words = []
for i in range(len(data['text'])):
    word = data['text'][i].strip()
    conf = int(data['conf'][i])

    if word != "" and conf > 0:
        valid_words.append((word, conf))
        status = "PASS" if conf >= 80 else "LOW "
        print(f"  [{status}] | Confidence: {conf:3}% | Word: '{word}'")

# --- STEP 5: FINAL SUMMARY ---
print("\n" + "="*50)
if valid_words:
    avg_confidence = sum(c for _, c in valid_words) / len(valid_words)
    passing = [w for w, c in valid_words if c >= 80]

    print(f"  Total words detected : {len(valid_words)}")
    print(f"  Words above 80%      : {len(passing)}")
    print(f"  Average confidence   : {avg_confidence:.1f}%")

    if avg_confidence >= 80:
        print(f"\n  PROJECT VALIDATION PASSED! ({avg_confidence:.1f}% >= 80%)")
    else:
        print(f"\n  Below 80% threshold. Try improving pre-processing.")

    full_text = pytesseract.image_to_string(pil_image).strip()
    print("\n--- EXTRACTED TEXT ---")
    print(full_text)
    print("="*50)

else:
    print("  No words detected. Check your image.")
