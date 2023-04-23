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

# Open the link
base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()

# Login in the system

#login = 'wrong_username'
#password_all = 'secret_sauce'


def login_in_system(login, password_all):
    user_name = driver.find_element(by=By.XPATH, value='//input[@id="user-name"]')
    user_name.send_keys(login)
    print("Input login")
    password = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
    password.send_keys(password_all)
    print("Input password")
    login_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')
    login_button.click()
    print("Click login button")


# Error message while wrong username or password

def get_warning_message(text):
    warning_text = driver.find_element(by=By.XPATH, value='//h3[@data-test="error"]')
    value_warning_text = warning_text.text
    assert value_warning_text == text, 'Wrong warning message displayed'


login_in_system('wrongusername', 'wrongpassword')
get_warning_message('Epic sadface: Username and password do not match any user in this service')
print('Test passed: Username and password do not match any user in this service')
driver.refresh() # обновить страницу
time.sleep(5)

# Error message while password required

login_in_system('standard_user', '')
get_warning_message('Epic sadface: Password is required')
print('Test passed: Password is required')
driver.refresh()
time.sleep(5)

# Error message while username required

login_in_system('', '')
get_warning_message('Epic sadface: Username is required')
print('Test passed: Username is required')
time.sleep(5)

login_in_system('', 'secret_sauce')
get_warning_message('Epic sadface: Username is required')
print('Test passed: Username is required')


