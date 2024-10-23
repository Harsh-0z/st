from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()  
try:
    
    driver.get("https://www.google.com")

    
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    
    search_term = "Selenium WebDriver"
    search_box.send_keys(search_term)
    search_box.submit()  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    print(f"Search for '{search_term}' completed successfully!")

finally:
   
    time.sleep(5)
    driver.quit()
