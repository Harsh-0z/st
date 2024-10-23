from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

try:
  
    driver.get("https://demoqa.com/buttons")

 
    actions = ActionChains(driver)


    button = driver.find_element(By.ID, "doubleClickBtn")

    
    actions.double_click(button).perform()
    print("Double-clicked the button!")

  
    right_click_button = driver.find_element(By.ID, "rightClickBtn")

    actions.context_click(right_click_button).perform()
    print("Right-clicked the button!")

finally:
  
    time.sleep(2)
    driver.quit()
