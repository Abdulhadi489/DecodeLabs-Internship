# DecodeLabs AI Engineering Internship 

Welcome to my portfolio repository for the DecodeLabs AI Engineering Internship. This repository tracks my weekly progress, algorithms, and projects as I build practical Artificial Intelligence and Computer Vision pipelines.

##  About the Developer
I am a 6th-semester Computer Science student and AI Enthusiast. I specialize in building robust backend pipelines, integrating machine learning models, and exploring agentic reasoning in software development.

##  Core Tech Stack Used
* **Languages:** Python
* **Machine Learning:** Scikit-learn (`TfidfVectorizer`, `cosine_similarity`)
* **Computer Vision:** OpenCV (`cv2`), PyTesseract, Pillow (`PIL`)
* **Data Processing:** NumPy

##  Project Breakdown

### [Week 1] Rule-Based Conversational Agent
A foundational interactive chatbot that demonstrates core application logic, control flow, and user input handling.
* **Control Flow:** Implemented a continuous `while` loop architecture to sustain ongoing user interaction until an explicit exit command is triggered.
* **Data Structures:** Utilized Python dictionaries for direct intent-to-response mapping, creating a lightweight baseline for conversational AI.
* **Data Sanitization:** Engineered early data cleaning logic (`.lower().strip()`) to standardize unpredictable user inputs before processing.
* **Error Handling:** Applied the `.get()` method with fallback responses to gracefully handle out-of-scope queries without breaking the application.

### [Week 3] Tech Stack Recommender Engine
A functional recommendation system that matches a user's skills to ideal job profiles. 
* Solved the "User Cold Start" problem with a sanitized ingestion pipeline.
* Leveraged **TF-IDF Vectorization** to convert text data into mathematical vocabulary.
* Utilized **Cosine Similarity** algorithms to calculate the exact match percentages between candidates and roles.

### [Week 4] Optical Character Recognition (OCR) Pipeline
A production-ready Computer Vision script that cleans images and extracts text with automated validation.
* **Pre-processing:** Applied Grayscale conversion, Gaussian Blur for noise reduction, and Otsu Thresholding for pure binary contrast.
* **Extraction:** Implemented Tesseract OCR to read text from custom-generated invoice images.
* **Validation:** Built a custom confidence-scoring loop to evaluate the accuracy of the extracted dictionary data against an 80% passing threshold.

---
*Developed during the 2026 DecodeLabs AI Training Program.*