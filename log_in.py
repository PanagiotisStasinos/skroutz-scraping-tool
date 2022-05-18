import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogIn:
    def __init__(self, driver, method):
        try:
            login_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/header/div/ul/li[1]/a"))
            )
            login_element.send_keys(Keys.RETURN)
        except:
            print("Unable to click login")
            return

        os.system("pause")

        if method == "email":
            try:
                email_form = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/form/div/div/input"))
                )
                email_form.send_keys("**********@gmail.com")
                email_form.send_keys(Keys.RETURN)
            except:
                print("Unable to give email")
            try:
                password_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/form/div[2]/div/div/input"))
                )
                password_input.send_keys("************")
                password_input.send_keys(Keys.RETURN)
            except:
                print("Unable to give password")
        elif method == "google":  # not implemented yet 18/5/22
            try:
                email_form = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div[1]/ul/li[1]/form/button"))
                )
                email_form.send_keys(Keys.RETURN)
            except:
                print("Unable to connect via google account")

            os.system("pause")

            try:
                input_email = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
                )
                input_email.send_keys("**********@gmail.com")
                input_email.send_keys(Keys.RETURN)
            except:
                print("Unable to give email")
