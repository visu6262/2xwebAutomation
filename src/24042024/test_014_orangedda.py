from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drive_360():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    username_ele = driver.find_element(By.NAME,"username").send_keys("Admin")
    password_ele = driver.find_element(By.NAME,"password").send_keys("admin12")

    button_ele = driver.find_element(By.XPATH,"//button[@type='submit']")
    button_ele.click()

    url1 = driver.current_url
    assert url1 == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    if url1 =="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
        finder = driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        print("login success")
        print(finder.text)
    else:
        url1 == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        finter1 = driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
        print("Login Invalid")
        print(finter1.text)

    driver.quit()

