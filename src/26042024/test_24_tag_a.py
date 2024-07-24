from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import os
from selenium.webdriver.common.action_chains import ActionChains
import requests


def test_borken_links():
    driver = webdriver.Chrome()
    driver.get("https://manaoorumanabadi.telangana.gov.in/momb/")
    driver.maximize_window()
    # driver.set_window_size(5160,3000)
    act = ActionChains(driver)
    links = driver.find_elements(By.TAG_NAME, "a")
    print(len(links))

    count = 0
    used_li = 0
    for link in links:
        url = link.get_attribute("href")
        try:
            res = requests.head(url)
        except:
            None

        if res.status_code >= 400:
            print(url, "borken link")
            count = count + 1
        else:
            print(url, "Narmal link")
            used_li = used_li + 1

    print("borken link count is", count)
    print("used link count is", used_li)

    allure.attach(driver.get_screenshot_as_png(), name="stage name", attachment_type=AttachmentType.PNG)
    # time.sleep(3)
    driver.quit()