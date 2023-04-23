import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# НЕЯВНОЕ ожидание
'''
Неявное ожидание - ждем, что наш элемент появится в DOM, и начинаем с ним работать, как только он там появится
Мы указываем время, в течение которого система ожидает наш элемент
При этом, если элемент появится раньше, то с ним раньше и начнем работать
(в отличие от time.sleep(), где пока указанное время не пройдет полностью, нам придется ждать и только потом работать с элементом)

И ещё, тот же time.sleep() мы указываем в каждом нужном месте
А driver.implicitly_wait() мы указываем один раз, а затем это применяется ко всему коду (к каждому действию)
'''
# driver.implicitly_wait(10)

# print('Start test')
# visible_button = driver.find_element(by=By.XPATH, value='//button[@id="visibleAfter"]')
# visible_button.click()
# print('"Visible after 5 seconds" button click')
# print('Finish test')

# ЯВНОЕ ожидание
'''
Мы можем начинать работать с элементом, как только он Visible/Clickable/... 
Тут мы можем использовать явное ожидание
Оно используется для конкретного нужного элемента, а не для всего и сразу, как driver.implicitly_wait()

Явное и неявное ожидание нельзя использовать одновременно
Ибо они перебивают работу друг друга 

WebDriverWait(driver, 30): мы будем взаимодействовать с нашим элементом в течение указанного времени (30 сек), 
попытыки тыкнуть кнопку будут повторятся каждые 0.5 сек. по умолчанию

EC = 'expected_condition' (условия, которые мы ожидаем, чтоб начать взаимодействовать с элементом)
from selenium.webdriver.support import expected_conditions as EC
'''
# print('Start test')
# wait_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="enableAfter"]')))
# wait_button.click()
# print('"Will enable 5 seconds" button click')
# print('Finish test')

visible_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="visibleAfter"]')))
visible_button.click()
print('"Visible after 5 seconds" button click')

