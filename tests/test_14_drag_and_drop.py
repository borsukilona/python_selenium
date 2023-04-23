import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
path = '/chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(options=options, service=service)

# -----------------------------------------------------------
# Open the link

driver.get('https://demoqa.com/')
driver.maximize_window()

# -----------------------------------------------------------
# Go to Interactions

interactions = driver.find_element(by=By.XPATH, value='//h5[text()="Interactions"]')
interactions.click()
print('Interactions click')

# Go to Interactions Menu

interactions_menu = driver.find_element(by=By.XPATH, value='//div[text()="Interactions"]')
interactions_menu.click()
time.sleep(2)
print('Interactions menu click')

# Go to Droppable menu point

driver.execute_script("window.scrollTo(0, 150)")
droppable_menu = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[4]')
droppable_menu.click()
print('Data Picker menu point click')

# Drag and drop perform

drag_element = driver.find_element(by=By.XPATH, value='//div[@id="draggable"]')
drop_here_element = driver.find_element(by=By.XPATH, value='//div[@id="droppable"]')
time.sleep(3)
actions = ActionChains(driver)
actions.drag_and_drop(drag_element, drop_here_element).perform()
print('Drag and drop performed')




