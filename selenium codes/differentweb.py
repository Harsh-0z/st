from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def launch_chrome():
    driver = webdriver.Chrome()
    return driver


def launch_firefox():
    driver = webdriver.Firefox()
    return driver


def launch_edge():
    driver = webdriver.Edge()
    return driver

def test_browser(driver, browser_name):
    try:
     
        driver.get("https://www.amazon.com")

        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
        )

     
        print(f"Website loaded successfully in {browser_name}!")

 
        driver.refresh()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
        )

   
        print(f"Website refreshed successfully in {browser_name}!")

    finally:
       
        time.sleep(3)
        driver.quit()


chrome_driver = launch_chrome()
test_browser(chrome_driver, "Chrome")


firefox_driver = launch_firefox()
test_browser(firefox_driver, "Firefox")


edge_driver = launch_edge()
test_browser(edge_driver, "Edge")
