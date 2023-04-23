from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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

# Go to Elements

elements = driver.find_element(by=By.XPATH, value='//div[text()="Elements"] ')
elements.click()
time.sleep(2)
print('Elements click')

# Go to Check Box menu point

checkbox_menu = driver.find_element(by=By.XPATH, value='//li[@id="item-1"]')
checkbox_menu.click()
print('Check-box menu point click')

# Click check box

checkbox_home = driver.find_element(by=By.XPATH, value='//span[@class="rct-checkbox"]')
checkbox_home.click()
print('Check-box Home click')

select_checkbox_home = driver.find_element(by=By.XPATH, value='//input[@id="tree-node-home"]')
print(f'---Is checkbox enabled after clicking - {select_checkbox_home.is_selected()}---')  # True if the element is selected and False if not

# Open home check box relatives

open_list_button = driver.find_element(by=By.XPATH, value='//button[@aria-label="Toggle"]')
open_list_button.click()
print('Open other check-boxes click')

# Go to Radio Button menu point
time.sleep(2)

radio_button_menu = driver.find_element(by=By.XPATH, value='//li[@id="item-2"]')
radio_button_menu.click()
print('Radio button menu point click')
time.sleep(2)

# Click Yes radio button

radio_button_yes = driver.find_element(by=By.XPATH, value='//label[@for="yesRadio"]')
radio_button_yes.click()
print('Radio button YES selected')

select_radio_button_yes = driver.find_element(by=By.XPATH, value='//input[@id="yesRadio"]')
print(f'---Is radio button enabled after clicking - {radio_button_yes.is_enabled()}---') # True if radio-button enabled and False if not
time.sleep(2)

driver.refresh() # reload the page
print("Paged reload")