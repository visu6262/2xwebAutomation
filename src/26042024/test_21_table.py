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

def test_table():
    driver = webdriver.Chrome()
    driver.get("https://cosmocode.io/automation-practice-webtable/")
    driver.maximize_window()
    time.sleep(4)

    rows = driver.find_elements(By.XPATH,"//table[@id='countries']//tr")
    no_of_rows = len(rows)
    print(no_of_rows)

    count = 0
    for r in range(1,no_of_rows+1):
        Currency = driver.find_element(By.XPATH,"//table[@id='countries']//tr["+str(r)+"]/td[4]").text
        Country = driver.find_element(By.XPATH,"//table[@id='countries']//tr["+str(r)+"]/td[2]").text
        print(Country,"=>",Currency,"\n")

        # if data == "Euro":
        #     one = driver.find_element(By.XPATH,"//table[@id='countries']//tr["+str(r)+"]/td[2]").text
        #     two = driver.find_element(By.XPATH,"//table[@id='countries']//tr["+str(r)+"]/td[3]").text
        #
        #     three = driver.find_element(By.XPATH,"//table[@id='countries']//tr["+str(r)+"]/td[5]").text
        #     print(one,two,data,three,end=" ")
        #     count=count+1
        # print()
    print("total count is:",count)

    driver.quit()
