from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_vwo_login():
    url="https://app.vwo.com/"
    driver=webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)