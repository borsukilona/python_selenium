from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

path = "C:\\Users\\Ilona\\Documents\\Python_Selenium\\gekodriver.exe"
service = Service(path)
driver = webdriver.Firefox(service=service)

# -----------------------------------------------------------
# Open the link

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# -----------------------------------------------------------
# Login in the system

'''
user_name = driver.find_element(by=By.XPATH, value='//input[@data-test="username"]')
user_name.send_keys('standard_user')

password = driver.find_element(by=By.CSS_SELECTOR, value='#password')
password.send_keys('secret_sauce')

login_button = driver.find_element(by=By.XPATH, value='//input[@value="Login"]')
login_button.click()

time.sleep(10) # wait for 5 sec and then close
driver.close()
'''

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





