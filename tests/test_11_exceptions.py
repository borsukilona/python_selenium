import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
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

# Go to Dynamic Properties menu point

driver.execute_script("window.scrollTo(0, 100)")

dynamic_properties = driver.find_element(by=By.XPATH, value='//li[@id="item-8"]')
dynamic_properties.click()
print('Dynamic Properties menu point click')

# "Visible after 5 seconds" button click

try:
    visible_button = driver.find_element(by=By.XPATH, value='//button[@id="visibleAfter"]')
    visible_button.click()
except NoSuchElementException as exception:
    print('NoSuchElementException')
    time.sleep(6)
    visible_button = driver.find_element(by=By.XPATH, value='//button[@id="visibleAfter"]')
    visible_button.click()
finally:
    print('"Visible after 5 seconds" button click')

# Go to Radio Button menu point
time.sleep(2)

radio_button_menu = driver.find_element(by=By.XPATH, value='//li[@id="item-2"]')
radio_button_menu.click()
print('Radio button menu point click')
time.sleep(2)

# Click Yes radio button

radio_button_yes = driver.find_element(by=By.XPATH, value='//label[@for="yesRadio"]')
radio_button_yes.click()
print('Radio button YES selected')

'''
Мы будем предполагать, что после нажатия радиобаттона мы ожидаем сообщение NO
Чисто чтоб потренироваться 
Благодаря этому отловим исключение
Обработаем его
Повторно нажмем на кнопку и будем ожидать уже то, что и должны (Yes)
И посмотрим как оно работает всё
'''

try:
    message_after_yes_clicking = driver.find_element(by=By.XPATH, value='//span[@class="text-success"]')
    time.sleep(2)
    value_text_after_yes_clicking = message_after_yes_clicking.text # Yes
    print(value_text_after_yes_clicking)
    assert value_text_after_yes_clicking == 'NO'
except AssertionError as exception:
    print('"NO" message expected')
    driver.refresh() # перезагружаем страничку
    print("Refresh the page")
    radio_button_yes = driver.find_element(by=By.XPATH, value='//label[@for="yesRadio"]')
    radio_button_yes.click()
    print('Radio button YES selected')
    message_after_yes_clicking = driver.find_element(by=By.XPATH, value='//span[@class="text-success"]')
    time.sleep(2)
    value_text_after_yes_clicking = message_after_yes_clicking.text  # Yes
    print(value_text_after_yes_clicking)
    assert value_text_after_yes_clicking == 'Yes'
    print(f'Radiobutton with value YES clicked and message {value_text_after_yes_clicking} disaplayed')


