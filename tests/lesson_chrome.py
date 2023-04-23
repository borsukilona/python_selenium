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

# user_name = driver.find_element(by=By.ID, value='user-name') # ID
# user_name = driver.find_element(by=By.NAME, value='user-name') # Name
# user_name = driver.find_element(by=By.XPATH, value='//*[@id="user-name"]') # Full XPATH * значит что мы обращаемся к любому элементу с id="user-name"
# user_name = driver.find_element(by=By.XPATH, value='//input[@id="user-name"]') # ID XPATH тут мы указали, что хотим именно input элемент с  id="user-name"

user_name = driver.find_element(by=By.XPATH, value='//input[@data-test="username"]') # data-test XPATH
user_name.send_keys('standard_user')

# password = driver.find_element(by=By.ID, value='password') # ID
password = driver.find_element(by=By.CSS_SELECTOR, value='#password') # CSS_SELECTOR
password.send_keys('secret_sauce')

# login_button = driver.find_element(by=By.ID, value='login-button') # ID
login_button = driver.find_element(by=By.XPATH, value='//input[@value="Login"]') # value XPATH
login_button.click()
# -----------------------------------------------------------



#time.sleep(5) # wait for 5 sec and then close
#driver.close()

