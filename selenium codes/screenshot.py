from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:

    driver.get("https://demoqa.com/elements")

 
    time.sleep(2)

    element = driver.find_element(By.XPATH, "//div[@class='element-list collapse show']")


    driver.save_screenshot("full_screenshot.png")


    location = element.location
    size = element.size


    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    from PIL import Image

    full_screenshot = Image.open("full_screenshot.png")
    partial_screenshot = full_screenshot.crop((left, top, right, bottom))
    partial_screenshot.save("partial_screenshot.png")

    print("Partial screenshot captured and saved as 'partial_screenshot.png'.")

finally:
    
    time.sleep(2)
    driver.quit()
