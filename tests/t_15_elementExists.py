import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
    login_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')
    login_button.click()
    print("Click login button")


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        print("No such element on the page")
        return False
    print("Element exists - TRUE")
    return True


login_in_system(login, password_all)

'''
Add product 1 to the cart
'''

select_product_1 = driver.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Product in the cart")

cart_badge = '//span[@class="shopping_cart_badge"]'

check_exists_by_xpath(cart_badge)