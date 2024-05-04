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

def test_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/")
    driver.maximize_window()
    time.sleep(4)
    # alert = driver.switch_to.alert
    # alert.accept()

    driver.find_element(By.XPATH,"//a[@title='India']").click()
    states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g'][1]/*[name()='path']")
    for state in states:
        print(state.get_attribute("aria-label"))
        if "Andhra Pradesh" in state.get_attribute("aria-label"):
            state.click()
            # break
    allure.attach(driver.get_screenshot_as_png(),name="stage name",attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()