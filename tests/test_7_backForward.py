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

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# -----------------------------------------------------------
# Login in the system

login = 'standard_user'
password_all = 'secret_sauce'


def login_in_system(login, password_all):
    user_name = driver.find_element(by=By.XPATH, value='//input[@id="user-name"]')
    user_name.send_keys(login)
    print("Input login")
    password = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
    password.send_keys(password_all)
    print("Input password")
    password.send_keys(Keys.RETURN)


login_in_system(login, password_all)
print('Login in the system')

time.sleep(3)

driver.back() # <-
print('Go back')
time.sleep(3)
driver.forward() # ->
print('Go forward')





