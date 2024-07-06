from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def is_google_account(email):
    # Inisialisasi WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
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

# Contoh penggunaan
email = "m.rezahidayat.rh@gmail.com"
if is_google_account(email):
    print(f"Email {email} terkait dengan akun Google")
else:
    print(f"Email {email} tidak terkait dengan akun Google")