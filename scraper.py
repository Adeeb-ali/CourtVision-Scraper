import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import pytesseract
import os
#Here, you have to put the path where your Tesseract OCR is installed on your system
#yaha aap ko apna path dalne ha jaha aap ke Tesseract  downmload kya ha   
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class ECourtsScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_site(self):
        self.driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")
        time.sleep(2)

    def solve_captcha(self):
        try:
            captcha_element = self.driver.find_element(By.ID, "captcha_image")
            captcha_path = "captcha.png"
            captcha_element.screenshot(captcha_path)

            # Convert to grayscale for OCR
            image = Image.open(captcha_path).convert("L")

            # OCR
            captcha_text = pytesseract.image_to_string(image, config='--psm 7').strip()
            print("[INFO] OCR Result:", captcha_text)

            input_box = self.driver.find_element(By.ID, "fcaptcha_code")
            input_box.clear()
            input_box.send_keys(captcha_text)

            return captcha_text
        except Exception as e:
            print(f"[WARN] OCR failed: {e}")
            return None

    def search_case(self, cnr_number):
        self.driver.find_element(By.ID, "cino").send_keys(cnr_number)
        time.sleep(2)

     
        captcha_text = self.solve_captcha()
        if not captcha_text or len(captcha_text) < 3:
            print("[INFO] OCR failed or low confidence. Please type captcha manually within 30 seconds.")
            time.sleep(30) 

      
        self.driver.find_element(By.ID, "searchbtn").click()
        print("[INFO] Search button clicked")
        time.sleep(5)

    def get_all_case_details(self):
        cases = []
        try:
            rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 4:
                    case = {
                        "serial": cells[0].text.strip(),
                        "court_name": cells[1].text.strip(),
                        "status": cells[2].text.strip(),
                        "pdf_link": cells[3].find_element(By.TAG_NAME, "a").get_attribute("href") if cells[3].find_elements(By.TAG_NAME, "a") else "N/A"
                    }
                    cases.append(case)
            return cases
        except:
            return []

    def close(self):
        self.driver.quit()
