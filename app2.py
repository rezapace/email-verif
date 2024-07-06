from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def is_google_account(email):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Jalankan dalam mode headless

    # Inisialisasi WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Buka halaman login Google
        driver.get("https://accounts.google.com/")

        # Masukkan email
        email_input = driver.find_element(By.ID, "identifierId")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Tunggu sebentar untuk memuat halaman berikutnya

        # Periksa jika ada pesan error
        try:
            error_message = driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
            if error_message.is_displayed():
                return False
        except:
            pass

        return True
    finally:
        driver.quit()

def process_email_list(file_path):
    results = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            email = line.strip()
            if is_google_account(email):
                results.append(f"Email {email} terkait dengan akun Google")
            else:
                results.append(f"Email {email} tidak terkait dengan akun Google")

    with open('output.txt', 'w') as output_file:
        for result in results:
            output_file.write(result + '\n')

# Path ke file yang berisi daftar email
file_path = 'email_list.txt'
process_email_list(file_path)
