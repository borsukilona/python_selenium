import datetime

from selenium import webdriver
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

driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')
driver.maximize_window()
# -----------------------------------------------------------
'''
click_and_hold() - кликаем и удерживаем мышь
move_by_offset(X, Y) - тянем: X по горизонтали, Y по ветикали
release() - отпускаем мышь

perform() нужен, чтобы вся наша цепочка команд actions начала работать (как зеленый свет к действиям)
'''

action = ActionChains(driver)

toddler = driver.find_element(by=By.XPATH, value='//input[@id="id2"]')
action.click_and_hold(toddler).move_by_offset(-550, 0).release().perform()


