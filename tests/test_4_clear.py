import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
path = '/chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(options=options, service=service)

# Open the link
base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()

# Login in the system

login = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(by=By.XPATH, value='//input[@id="user-name"]')
user_name.send_keys(login)
print("Input login")
'''
password = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
password.send_keys(password_all)
print("Input password")
login_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')
login_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')
login_button.click()
print("Click login button")
'''

# Clear the field

time.sleep(5)
user_name.clear()



