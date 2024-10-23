from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# Initialize WebDriver (for Chrome in this case)
driver = webdriver.Chrome()

try:
    ### Handling Drop Down ###
    # Navigate to the demo website for dropdown
    driver.get("https://demoqa.com/select-menu")
    
    # Wait for the dropdown to be visible and select an option
    dropdown = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "oldSelectMenu"))
    ))
    dropdown.select_by_visible_text("Blue")
    print("Dropdown option selected.")

    ### Handling File Upload ###
    # Navigate to file upload example page
    driver.get("https://demoqa.com/upload-download")

    # Provide the full path to the file you want to upload
    file_input = driver.find_element(By.ID, "uploadFile")
    file_input.send_keys(os.path.abspath("path_to_your_file.txt"))  # Replace with your file path
    print("File uploaded successfully.")

    ### Handling Alerts and Popups ###
    # Navigate to alert example page
    driver.get("https://demoqa.com/alerts")

    # Click to trigger a simple alert
    driver.find_element(By.ID, "alertButton").click()
    
    # Wait for the alert and accept it
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    print("Alert handled successfully.")

    ### Handling Multiple Windows ###
    # Navigate to multiple windows example
    driver.get("https://demoqa.com/browser-windows")

    # Click to open a new window
    driver.find_element(By.ID, "windowButton").click()
    
    # Get the handle of the main window
    main_window = driver.current_window_handle

    # Wait for the new window, then switch to it
    WebDriverWait(driver, 10).until(EC.new_window_is_opened)
    windows = driver.window_handles
    for window in windows:
        if window != main_window:
            driver.switch_to.window(window)
            print("Switched to new window.")

    # Close the new window and switch back to the main window
    driver.close()
    driver.switch_to.window(main_window)
    print("Closed new window and switched back to the main window.")

    ### Mouse Hover ###
    # Navigate to mouse hover example page
    driver.get("https://demoqa.com/tool-tips")

    # Perform mouse hover over an element
    hover_element = driver.find_element(By.ID, "toolTipButton")
    action = ActionChains(driver)
    action.move_to_element(hover_element).perform()
    print("Mouse hover performed.")

    ### Mouse Right Click ###
    # Right-click on an element
    action.context_click(hover_element).perform()
    print("Mouse right-click performed.")

    ### Mouse Double Click ###
    # Double-click on the same element
    action.double_click(hover_element).perform()
    print("Mouse double-click performed.")

    ### Drag and Drop ###
    # Navigate to drag and drop example
    driver.get("https://demoqa.com/droppable")

    # Locate source and target elements
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    # Perform drag and drop action
    action.drag_and_drop(source, target).perform()
    print("Drag and drop performed.")

finally:
    # Close the browser after a short delay
    time.sleep(5)
    driver.quit()
