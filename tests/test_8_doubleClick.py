from selenium import webdriver
from selenium.webdriver import ActionChains
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

# Go to Buttons menu point

buttons_menu = driver.find_element(by=By.XPATH, value='//li[@id="item-4"]')
buttons_menu.click()
print('Buttons menu point click')

# Double click

action = ActionChains(driver) # в этом классе селениума есть много полезных функций, в том числе и наш double click
double_click_button = driver.find_element(by=By.XPATH, value='//button[@id="doubleClickBtn"]')
action.double_click(double_click_button).perform() # perform() нужен, чтоб сохранить действие двойного клика
print('Double click occurs')

# Right click

right_click_button = driver.find_element(by=By.XPATH, value='//button[@id="rightClickBtn"]')
action.context_click(right_click_button).perform()
print('Right click occurs')

