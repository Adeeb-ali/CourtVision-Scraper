Ah! I see exactly what you mean — you want a **real GitHub-style README**, the kind that is **clean, visually structured, easy to read, with proper headings, badges, code blocks, and “understandable” explanations**, not just a plain doc. Let me rewrite it in **professional GitHub format**.

---

# 🏛️ eCourts Scraper

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) ![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium) ![Tesseract](https://img.shields.io/badge/Tesseract-OCR-orange?logo=tesseract) ![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 📖 Overview

**eCourts Scraper** is a Python-based automation tool designed to **scrape case details** from the official [eCourts India portal](https://services.ecourts.gov.in/ecourtindia_v6/).

This project was developed as a **student assignment** to automate the process of fetching case information using a **CNR (Case Number Record) number**.

The scraper handles:

* Automatic captcha recognition using **Tesseract OCR**
* Manual captcha entry if OCR fails
* Extracting **case details**, including serial number, court name, status, and PDF links

---

## ⚡ Features

* ✅ Fully automated Chrome browser interaction using **Selenium**
* ✅ CNR-based case search
* ✅ Captcha recognition (automatic OCR or manual input)
* ✅ Extracts and displays case information in a structured format
* ✅ Easy to extend: save results to **CSV, database, or JSON**

---

## 🗂 Project Structure

```
src/
│
├─ scraper.py       # Main scraper class
├─ main.py          # Optional runner script
└─ captcha.png      # Temporary screenshot for captcha (generated dynamically)
```

---

## 🛠 Prerequisites

1. **Python 3.8+**
2. **Google Chrome** installed
3. **Tesseract OCR** installed

   * Windows default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`
   * [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)
4. Python packages:

```bash
pip install selenium webdriver-manager pillow pytesseract
```

---

## 🚀 How to Use

1. **Clone the repository**

```bash
git clone <your-github-repo-link>
cd <repo-folder>
```

2. **Run the scraper**

```python
from src.scraper import ECourtsScraper

# Initialize scraper
scraper = ECourtsScraper()

# Open eCourts portal
scraper.open_site()

# Search a case by CNR number
scraper.search_case("DL010001232021")  # Replace with your CNR

# Fetch all case details
cases = scraper.get_all_case_details()
for case in cases:
    print(case)

# Close browser
scraper.close()
```

3. **Manual Captcha Handling**
   If OCR fails or has low confidence, you will have **30 seconds to enter the captcha manually**.

---

## 🧠 How It Works

1. Open the **eCourts India website** using Selenium Chrome WebDriver.
2. Enter the **CNR number** in the input box.
3. Capture the **captcha image** and use Tesseract OCR to recognize text.
4. Fill the captcha automatically or manually (if OCR fails).
5. Click **Search** and wait for results.
6. Scrape the results table for:

   * Serial number
   * Court name
   * Case status
   * PDF link (if available)

---

