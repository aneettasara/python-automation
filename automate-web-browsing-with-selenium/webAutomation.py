from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')
# Maximize Browser
driver.maximize_window()
# Explicit Wait for element to be visible
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'firstName')))
# Input Value
firstName = driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys('Sara')
# Click Element
gender = driver.find_element_by_xpath('//*[@id="genterWrapper"]/div[2]/div[2]/label')
gender.click()
# Implicit Wait
driver.implicitly_wait(10)
# Redirect to another Url
driver.get('https://demoqa.com/droppable') 
# Explicit Wait for element to be visible
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'draggable')))
# Drag and Drop
source = driver.find_element_by_xpath('//*[@id="draggable"]')
destination = driver.find_element_by_xpath('//*[@id="droppable"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# Implicit Wait
driver.implicitly_wait(10)
# Closes the current window
driver.close()
