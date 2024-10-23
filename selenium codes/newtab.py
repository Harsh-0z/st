from selenium import webdriver
import time


driver = webdriver.Chrome()

try:
    
    driver.get("https://www.example.com")
    
    
    driver.execute_script("window.open('https://www.google.com', '_blank');")
    
    
    time.sleep(5)

  
    driver.switch_to.window(driver.window_handles[1])

    
    time.sleep(5)
    
   
    print("Google is now open in a new tab!")

finally:
    
    time.sleep(2)
    driver.quit()
