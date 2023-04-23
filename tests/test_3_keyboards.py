from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

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


def login_in_system(login, password_all):
    user_name = driver.find_element(by=By.XPATH, value='//input[@id="user-name"]')
    user_name.send_keys(login)
    print("Input login")
    password = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
    password.send_keys(password_all)
    print("Input password")
    #login_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')
    #login_button.click()
    #print("Click login button")
    #user_name.send_keys(Keys.BACK_SPACE) #стираем последний символ
    #for _ in range(2): # если надо стереть больше символов, нам надо продублировать строку
    #    user_name.send_keys(Keys.BACK_SPACE)
    password.send_keys(Keys.RETURN) # ввели лоин, пароль и нажали Enter


login_in_system(login, password_all)

# Click down arrow


def use_filter():
    options_list = driver.find_elements(by=By.XPATH, value='//select[@data-test="product_sort_container"]/option')
    for i in range(1, len(options_list)):
        filter = driver.find_element(by=By.XPATH, value='//select[@data-test="product_sort_container"]')
        filter.click()
        print(f"Filter clicked {i}")
        time.sleep(2)
        filter.send_keys(Keys.DOWN)
        time.sleep(2)
        filter.send_keys(Keys.RETURN)
        time.sleep(2)


use_filter()
driver.close()



