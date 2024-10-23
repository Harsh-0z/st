from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()  
try:
   
    driver.get("https://www.amazon.com")

  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
    )

    
    print("Page loaded successfully!")

   
    driver.refresh()

  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
    )

    
    print("Page refreshed successfully!")

finally:
    
    time.sleep(5)
    driver.quit()
