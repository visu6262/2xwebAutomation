from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def test_vwologin():
    url = "https://app.vwo.com/"
    driver=webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    email_address_element=driver.find_element(By.ID,'login-username')
    email_address_element.send_keys('abc@gmail.com')

    pass_word=driver.find_element(By.ID,'login-password')
    pass_word.send_keys('admin@123')

    signin_element=driver.find_element(By.ID,'js-login-btn')
    signin_element.click()
    time.sleep(4)

    vwotitle=driver.title
    print("print 1",vwotitle)
    print(type(vwotitle))
    assert vwotitle == 'Login - VWO'

    error_msg_element=driver.find_element(By.ID,'js-notification-box-msg')
    print("print 2 ==>",error_msg_element.text)
    print(type(error_msg_element.text))
    assert error_msg_element.text == 'Your email, password, IP address or location did not match'
    time.sleep(4)

    current_url=driver.current_url
    print('print 3',current_url)
    assert current_url == 'https://app.vwo.com/#/login'