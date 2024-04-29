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


def upload_excel(file_path):
    uidpwd = []
    wb = openpyxl.load_workbook(file_path)
    sh = wb["Sheet1"]

    for row in sh.iter_rows(min_row=2, values_only=True):
        a, b = row
        uidpwd.append({
            "username": a,
            "password": b
        })
    return uidpwd


file_path = os.getcwd() + "/opensourceddt.xlsx"

@pytest.mark.parametrize("user_cred", upload_excel(file_path=file_path))
def test_open_url(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    # print(username, password)
    open_source(username=username,password=password)


def open_source(username, password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    username_ele = driver.find_element(By.NAME, "username").send_keys(username)
    password_ele = driver.find_element(By.NAME, "password").send_keys(password)

    button_ele = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_ele.click()

    result_url = driver.current_url
    # assert result_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    time.sleep(3)
    if result_url != "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        finter = driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
        print("Login Invalid")
        print(finter.text)
    else:
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        finder = driver.find_element(By.XPATH,
                                     "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        print("login success")
        print(finder.text)

        driver.quit()


