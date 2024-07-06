**app.py**
tidak bisa karena ketika memasukan password error walau sudah nunggu delay

**app1.py**
bisa namun harus list di program

**app2.py**
bisa menyimpan di email_list.txt dan outputnya di email_output.txt namun hanya 1 chrome 

**app3.py**
bisa melakukan multi threding dan hasil nya lebih bagus




1. **Buka Browser Chrome:** Pastikan Anda sudah masuk ke akun Google di browser Chrome Anda.
2. **Buka Halaman Login Google:** Kunjungi halaman login Google di [https://accounts.google.com/](https://accounts.google.com/).
3. **Gunakan Email yang Akan Divalidasi:** Masukkan email yang ingin Anda validasi di kolom email dan klik "Next".
4. **Perhatikan Respons dari Google:** Google akan memberikan respons apakah email tersebut valid atau tidak.

Berikut adalah langkah-langkah lebih rinci:

### Langkah 1: Buka Browser Chrome
Buka browser Chrome di komputer Anda.

### Langkah 2: Buka Halaman Login Google
Kunjungi halaman login Google di [https://accounts.google.com/](https://accounts.google.com/).

### Langkah 3: Masukkan Email
Masukkan email yang ingin Anda validasi, dalam kasus ini "208620600022@umsida.ac.id".

![Google Login Page](https://accounts.google.com/)

### Langkah 4: Perhatikan Respons dari Google
- **Email Valid:** Jika email tersebut valid dan terdaftar sebagai akun Google, Anda akan dibawa ke halaman berikutnya untuk memasukkan password.
- **Email Tidak Valid:** Jika email tidak valid atau tidak terdaftar sebagai akun Google, Anda akan mendapatkan pesan error seperti "Couldn't find your Google Account" atau pesan serupa yang menunjukkan bahwa email tersebut tidak terdaftar.

### Contoh Respons:
- **Email Valid:** Anda akan melihat halaman untuk memasukkan password.
- **Email Tidak Valid:** Anda akan melihat pesan error.

![Google Account Not Found](https://support.google.com/accounts/answer/6010255)

### Validasi Otomatis dengan Selenium
Jika Anda ingin mengotomatisasi proses ini menggunakan Selenium di Python, berikut adalah contoh skripnya:

### Instalasi Selenium
```bash
pip install selenium
```

### Script Python Menggunakan Selenium
```python
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
email = "208620600022@umsida.ac.id"
if is_google_account(email):
    print(f"Email {email} terkait dengan akun Google")
else:
    print(f"Email {email} tidak terkait dengan akun Google")
```

### Penjelasan Skrip:
1. **Inisialisasi WebDriver:** Menggunakan `webdriver_manager` untuk mengelola driver Chrome.
2. **Buka Halaman Login Google:** Buka halaman login Google.
3. **Masukkan Email:** Masukkan email yang ingin divalidasi.
4. **Periksa Respons:** Periksa apakah ada pesan error yang menunjukkan bahwa email tidak valid.

Pastikan Anda telah menginstal Chrome dan WebDriver sesuai dengan versi Chrome yang Anda gunakan. Skrip ini akan membuka browser Chrome, memasukkan email, dan memeriksa apakah email tersebut valid dengan melihat adanya pesan error atau tidak.