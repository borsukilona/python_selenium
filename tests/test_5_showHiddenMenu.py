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

login_in_system(login, password_all)

# Open hidden menu (burger-menu needs to be opened in order to see the menu points)

menu = driver.find_element(by=By.XPATH, value='//button[@id="react-burger-menu-btn"]')
menu.click()
print("Click burger menu")
time.sleep(2)
#link_about = driver.find_element(by=By.XPATH, value='//a[@id="about_sidebar_link"]')
link_about = driver.find_element(by=By.XPATH, value='//nav[@class="bm-item-list"]/a[2]')
link_about.click()
print("Click menu About")
time.sleep(2)
driver.back() # return to the previous page
link_logout = driver.find_element(by=By.XPATH, value='//nav[@class="bm-item-list"]/a[3]')
time.sleep(2)
link_logout.click()

login_in_system(login, password_all)
menu = driver.find_element(by=By.XPATH, value='//button[@id="react-burger-menu-btn"]')
menu.click()
time.sleep(2)
link_reset = driver.find_element(by=By.XPATH, value='//nav[@class="bm-item-list"]/a[4]')
time.sleep(2)
link_reset.click()








