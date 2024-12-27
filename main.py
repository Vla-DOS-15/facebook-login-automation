import os
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename="out.log", level=logging.INFO, format="%(asctime)s - %(message)s")

class FacebookLoginAutomation:
    def __init__(self, email, password, save_dir="data/logins_img/"):
        self.email = email
        self.password = password
        self.save_dir = save_dir
        self.driver = webdriver.Chrome()
        self._prepare_directory()

    def _prepare_directory(self):
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def login(self):
        try:
            self.driver.get("https://www.facebook.com/")
            logging.info("The login site is open")

            # Введення даних у форму входу
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            password_field = self.driver.find_element(By.ID, "pass")
            login_button = self.driver.find_element(By.NAME, "login") # Пробував By.ID але через декылька спроб згенерувалоь рандомне id

            username_field.send_keys(self.email)
            password_field.send_keys(self.password)
            logging.info("Login data entered")

            login_button.click()
            logging.info("The login button is clicked")
        except Exception as e:
            logging.error(f"An error occurred during login: {e}")
            self.driver.quit()
            raise

    def download_profile_picture(self):
        try:
            # Очікувати завантаження сторінки профілю
            profile_picture = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'image'))
            )
            profile_picture_url = profile_picture.get_attribute("xlink:href")
            logging.info(f"Profile picture URL: {profile_picture_url}")

            # Завантажуємо фотографію
            response = requests.get(profile_picture_url)
            if response.status_code == 200:
                file_path = os.path.join(self.save_dir, "profile_picture.jpg")
                with open(file_path, "wb") as file:
                    file.write(response.content)
                logging.info(f"Profile picture saved at: {file_path}")
            else:
                logging.error("Failed to download profile picture")
        except Exception as e:
            logging.error(f"An error occurred while downloading the profile picture: {e}")
            raise

    def close(self):
        self.driver.quit()
        logging.info("The browser is closed")

if __name__ == "__main__":
    phone_or_email = "replace by phone or email"
    password = "replace with a password"

    facebook_bot = FacebookLoginAutomation(phone_or_email, password)

    try:
        facebook_bot.login()
        facebook_bot.download_profile_picture()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        facebook_bot.close()
