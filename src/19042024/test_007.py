from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_ebay():
    url = "https://www.ebay.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID, "gh-ac").send_keys("16gb")
    driver.find_element(By.ID, "gh-btn").click()
    time.sleep(3)
    # list=driver.find_elements(By.TAG_NAME,"span")
    # print(len(list))
    # time.sleep(4)
    list_1 = driver.find_elements(By.XPATH, "//span[@role='heading']")
    list_2 = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    print(len(list_1))
    print(len(list_2))

    # // div[ @class ='s-item__info clearfix'] / a / div / span

    for i in list_1:
        text = i.text
        print(text)


    driver.quit()
