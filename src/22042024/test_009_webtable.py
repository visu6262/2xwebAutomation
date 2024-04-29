from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_ebay():
    url = "https://awesomeqa.com/webtable1.html"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    # // table[ @class ='tsc_table_s13'] / tbody / tr[1] / td[2]

    table=driver.find_element(By.XPATH,"//table[@class='tsc_table_s13']/tbody")
    row_table =table.find_elements(By.TAG_NAME,'tr')

    for row in row_table:
        cols=row.find_elements(By.TAG_NAME,'td')
        for j in cols:
            k=j.text
            print(k)




    driver.quit()