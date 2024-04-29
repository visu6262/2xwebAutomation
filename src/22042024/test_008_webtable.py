from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_ebay():
    url = "https://awesomeqa.com/webtable.html"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    row=driver.find_elements(By.XPATH,"//table[@id='customers']//tr")
    no_row =len(row)
    print("\nNo of Row's is :",no_row)

    col=driver.find_elements(By.XPATH,"//table[@id='customers']//tr[2]/td")
    no_col = len(col)
    print("No of Coloum's is :",no_col)

    # // table[ @ id = 'customers'] // tr[2] / td[3]

    first_step = "// table[ @ id = 'customers'] // tr["
                 # 2 ==> (i = 2 to 7)
    second_step = "] / td["
                 # 3 ==> (j = 1 to 3)
    threed_step = "]"

    for i in range(2,no_row+1):
        for j in range(1,no_col+1):
            path=f"{first_step}{i}{second_step}{j}{threed_step}"
            data=driver.find_element(By.XPATH,path).text
            print(data)
            if "Giovanni Rovelli" in data:
                current_path = path
                print(current_path)
                current_text= driver.find_element(By.XPATH,current_path).text
                print("Giovanni Rovelli self text is :",current_text)

                precedsib_path=f"{current_path}/preceding-sibling::td"
                precedsib_text = driver.find_element(By.XPATH,precedsib_path).text
                print("preceding-sibling of Giovanni Rovelli is :",precedsib_text)

                followingsib_path = f"{current_path}/following-sibling::td"
                followingsib_text = driver.find_element(By.XPATH,followingsib_path).text
                print("preceding-sibling of Giovanni Rovelli is :",followingsib_text)




    driver.quit()