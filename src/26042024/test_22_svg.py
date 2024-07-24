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

def test_svg():
    driver = webdriver.Chrome()
    driver.get("https://manaoorumanabadi.telangana.gov.in/momb/")
    driver.maximize_window()
    time.sleep(4)
    # alert = driver.switch_to.alert
    # alert.accept()
    count=0
    space=0

    state = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][6]/*[name()='g']/*[name()='text']/*[name()='tspan']")
    print(len(state))
    svgs= driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][3]/*[name()='g'][1]/*[name()='g'][1]/*[name()='path']")
    for dist in state:
        print(dist.text)
        count=count+1
        if " " in dist.text:
            space=space+1
            # print("==> dist in the state")
            pass
    print("total spaces",space)
    print("total",count)


    allure.attach(driver.get_screenshot_as_png(),name="stage name",attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()