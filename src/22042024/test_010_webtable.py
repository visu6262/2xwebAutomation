from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_ebay():
    url = "https://opensource-demo.orangehrmlive.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(5)
    admin_element=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
    admin_element.click()

    time.sleep(5)
    # // div[ @class ='oxd-table-body']/div[2]/div/div[2]
    one="// div[ @class ='oxd-table-body']/div["
        # 2 (i 1 to x)
    two="]/div/div["
        # 2 (j 1 to x)
    three = "]"

    row = driver.find_elements(By.XPATH,"// div[ @class ='oxd-table-body']/div")
    no_row = len(row)
    print(no_row)

    col= driver.find_elements(By.XPATH,"//div[ @class ='oxd-table-body']//div[2]/div/div")
    no_col = len(col)
    print(no_col)

    time.sleep(5)
    for i in range(1,no_row+1):
        for j in range(1,no_col+1):
            path=f"{one}{i}{two}{j}{three}"
            data=driver.find_element(By.XPATH,path).text
            print(data)
            if "106310" in data:
                current_path=path
                print(current_path)
                current_text = driver.find_element(By.XPATH,current_path).text
                print("current text is :",current_text)


    driver.quit()