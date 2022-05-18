import os   # os.system("pause") ,pausing for debugging reasons
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from skroutz_scraping_tool import log_in

if __name__ == "__main__":
    start_time = time.time()

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.skroutz.gr/")

    # os.system("pause")
    try:
        accept_all_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[7]/div/article[1]/div/form[1]/button'))
        )
        accept_all_item.send_keys(Keys.RETURN)
        # print("ACCEPT ALL ITEM - OK!")
    except:
        print("0 - ERROR! click accept all button failed")
        driver.quit()

    log_in.LogIn(driver, "email")

    os.system("pause")

    print("--- %s seconds ---" % (time.time() - start_time))
