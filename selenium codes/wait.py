from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


driver.implicitly_wait(10)  

try:
   
    driver.get("https://demoqa.com/select-menu")

    driver.execute_script("document.getElementById('oldSelectMenu').value = '2';") 
    print("Dropdown option selected using implicit wait.")

   
    driver.get("https://demoqa.com/alerts")

    
    driver.find_element(By.ID, "alertButton").click()

    WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()
    print("Alert handled using explicit wait.")

  
    driver.get("https://demoqa.com/progress-bar")
    

    driver.find_element(By.ID, "startStopButton").click()


    fluent_wait = WebDriverWait(driver, 30, poll_frequency=1)

  
    fluent_wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "progress-bar"), "100%"))
    print("Progress bar completed using fluent wait.")

finally:
    
    time.sleep(2)
    driver.quit()
