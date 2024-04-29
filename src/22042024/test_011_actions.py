import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_awesomeqa():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    action = ActionChains(driver)

    clickble = driver.find_element(By.ID,"clickable")
    # action.move_to_element(clickble).click().key_down(Keys.SHIFT).send_keys("viswanath").key_up(Keys.SHIFT).perform()
    action.key_down(Keys.SHIFT).send_keys_to_element(clickble,"viswanath").key_up(Keys.SHIFT).perform()
    clickble.send_keys("Komali")
    time.sleep(5)


    driver.quit()