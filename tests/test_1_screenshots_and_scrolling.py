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
password = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
password.send_keys(password_all)
print("Input password")
login_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')
login_button.click()
print("Click login button")

# Check if we on the right page

'''
text_products = driver.find_element(by=By.XPATH, value='//span[@class="title"]')
value_text_products = text_products.text #считали текст с нашего эелемнта на странице и сохранили в перменную
print(value_text_products) # PRODUCTS
assert value_text_products == 'PRODUCTS' # assert значит, что мы будем проводить сравнение (будет ошибка, если неравно: AssertionError)
print("The right page is opened")
'''

url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url # сохраняем ссылку той страницы, где мы находимся
print(get_url) # https://www.saucedemo.com/inventory.html
assert get_url == url
print("The right page is opened")
time.sleep(2)

# Make screenshot

'''
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = f'screenshot{now_date}.png'
driver.save_screenshot(f"C:\\Users\\Ilona\\Documents\\Python_Selenium\\Screen\\{name_screenshot}")
'''

# Scroll page / See the element
'''
driver.execute_script("window.scrollTo(X, Y)") 

скролим по координатам, измеряются в пикселях (0, 0 - верхний левый угол), 
X слева - вправо, Y - сверху - вниз

- если мы не видим какой-то элемент и надо проскролить
- скришнот скрытой области, надо спрокролить и заскринить
'''

# driver.execute_script("window.scrollTo(0, 500)")

action = ActionChains(driver) # показываем системе, что хотим управлять именно нашим драйвером
red_t_short = driver.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-onesie"]')
action.move_to_element(red_t_short).perform()
# перемещаемся к нашему элементу, который скрыт за скролингом (вместо execute_script("window.scrollTo(0, 500)"))

time.sleep(5)
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = f'screenshot{now_date}.png'
driver.save_screenshot(f"C:\\Users\\Ilona\\Documents\\Python_Selenium\\Screen\\{name_screenshot}")


