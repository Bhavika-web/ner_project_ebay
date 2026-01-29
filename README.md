# 🚗 eBay Car Title Named Entity Recognition (NER)

An AI-powered web application that automatically extracts structured information—like **Brand**, **Model**, **Parts**, and **Engine Specs**—from messy eBay car listing titles. Built using **spaCy** for custom NER training and **Streamlit** for the interactive user interface.

## 🌟 Features
- **Auto-Cleaning**: Handles raw eBay titles with underscores (e.g., `BMW_320d_Touring`).
- **Custom AI Model**: A spaCy pipeline specifically trained on automotive terminology to fix common misclassifications (like "Bumper" being called a Brand).
- **Entity Highlighting**: Visual labels for:
  - `BRAND` (e.g., Volkswagen, BMW)
  - `MODEL` (e.g., Golf, Astra G)
  - `PART` (e.g., Bumper, GTI)
  - `POWER` (e.g., 235 PS)
  - `YEAR` (e.g., 2016)

---

## 🛠️ Local Setup & Installation

Follow these steps to run the project on your own machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
2. Install Dependencies
Make sure you have Python installed. Then, install the required libraries:

Bash
pip install -r requirements.txt
3. Prepare the Data
Clean the raw auto.csv file to remove underscores and handle encoding issues:

Bash
python prepare_data.py
4. Train the AI Model
Train the custom spaCy NER model using the training script:

Bash
python train_ner.py
5. Launch the Web App
Run the Streamlit interface using the Python module command (this avoids "command not found" errors in PowerShell):

Bash
python -m streamlit run app.py
