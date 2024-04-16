from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_cura_healthcare_service():
    url="https://katalon-demo-cura.herokuapp.com/"
    driver=webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)

    current_url=driver.current_url
    print(current_url)
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"

    current_title=driver.title
    print(current_title)
    assert current_title == "CURA Healthcare Service"

    Make_Appointment_element=driver.find_element(By.ID,'btn-make-appointment')
    Make_Appointment_element.click()

    current_url1= driver.current_url
    print(current_url1)
    assert current_url1 == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    user_name_element=driver.find_element(By.ID,'txt-username')
    user_name_element.send_keys('John Doe')

    pass_word_element=driver.find_element(By.ID,'txt-password')
    pass_word_element.send_keys('ThisIsNotAPassword')

    login_button_click=driver.find_element(By.ID,'btn-login')
    login_button_click.click()

    current_url2 = driver.current_url
    print(current_url2)
    assert current_url2 == "https://katalon-demo-cura.herokuapp.com/#appointment"

    make_appointment_page_or_not=driver.find_element(By.XPATH,'//*[@id="appointment"]/div/div/div/h2')
    print(make_appointment_page_or_not.text)
    assert make_appointment_page_or_not.text == "Make Appointment"
    time.sleep(4)