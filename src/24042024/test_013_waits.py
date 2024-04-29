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

    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()

    email_element = driver.find_element(By.XPATH, "//input[@id='username']")
    email_element.send_keys('augtest_040823@idrive.com')

    pass_word_element = driver.find_element(By.XPATH, "//input[@id='password']")
    pass_word_element.send_keys('123456')

    signin_button_element = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    signin_button_element.click()

    driver_wait = WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[Exception])
    element1 = driver_wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='expiredmsg']/div/h5")))
    print(element1.text,'print element1')

    # time.sleep(20)
    msg_error_element = driver.find_element(By.XPATH,"//*[@id='expiredmsg']/div/h5")
    a = msg_error_element.text
    print("print 2",a)
    assert a == "Your free trial has expired"

    current_url2 = driver.current_url
    print("print 3", current_url2)
    assert current_url2 == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    allure.attach(driver.get_screenshot_as_png(), name='one', attachment_type=AttachmentType.PNG)
    driver.quit()
