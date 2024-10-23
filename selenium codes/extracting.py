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

   
    result_titles = driver.execute_script("""
        return Array.from(document.querySelectorAll('h3')).map(el => el.innerText);
    """)

    print("Search Results:")
    for title in result_titles:
        print(title)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
   
    time.sleep(5)
    driver.quit()
