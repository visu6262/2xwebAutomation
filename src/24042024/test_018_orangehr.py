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

def test_orange_hr():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    driver.switch_to.alert.accept()

    driver.find_element(By.XPATH,"//span[text()='Admin']").click()
    driver.find_element(By.XPATH,"//div[@class='orangehrm-header-container']/button[1]/text()[3]").click()
    driver.quit()