from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure


def test_drive_360():
    url = "https://www.idrive360.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    sigin_element = driver.find_element(By.LINK_TEXT, 'Sign In')
    sigin_element.click()
    current_url1 = driver.current_url
    print("print 1", current_url1)
    assert current_url1 == "https://www.idrive360.com/enterprise/login"

    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    time.sleep(3)

    email_element = driver.find_element(By.XPATH, "//input[@id='username']")
    email_element.send_keys('augtest_040823@idrive.com')

    pass_word_element = driver.find_element(By.XPATH, "//input[@id='password']")
    pass_word_element.send_keys('123456')

    signin_button_element = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    signin_button_element.click()
    time.sleep(30)

    msg_error_element = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div[2]/div[2]/app-account/section/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div/fieldset[1]/div[1]/div/h5")
    print("print 2", msg_error_element.text)
    assert msg_error_element.text == "Your free trial has expired"

    current_url2 = driver.current_url
    print("print 3", current_url2)
    assert current_url2 == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    allure.attach(driver.get_screenshot_as_png(), name='one', attachment_type=AttachmentType.PNG)
    time.sleep(5)
    driver.quit()
