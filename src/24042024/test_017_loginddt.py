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

def read_from_data_excel(file_path):
    uidpwd=[]
    wb = openpyxl.load_workbook(file_path)
    sh=wb["Sheet1"]
    for row in sh.iter_rows(min_row=2,values_only=True):
        a,b = row
        uidpwd.append({
            "username": a,
            "password": b
        })
    return uidpwd

file_path=os.getcwd() +"/Practicetestddt.xlsx"
print("file path iis ==>",file_path)

@pytest.mark.parametrize("user_cred",read_from_data_excel(file_path=file_path))
def test_ligin(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username,password)
    practice_login(username=username,password=password)


def practice_login(username,password):
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()

    success = 0
    fails = 0

    result = driver.current_url

    if result == "https://practicetestautomation.com/logged-in-successfully/":
        assert result == "https://practicetestautomation.com/logged-in-successfully/"
        finder = driver.find_element(By.XPATH, "//h1[text()='Logged In Successfully']")
        print(finder.text)
        driver.find_element(By.XPATH, "//a[text()='Log out']").click()
        success=success + 1
    else:
        driver.find_element(By.XPATH, "//div[@id='error']")
        fails=fails + 1



    print("Total Succesfully logins",success)
    print("Total Faild logins",fails)

    driver.quit()

