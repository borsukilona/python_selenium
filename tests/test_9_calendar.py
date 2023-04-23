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

driver.get('https://demoqa.com/')
driver.maximize_window()
# -----------------------------------------------------------
# Go to Interactions

interactions = driver.find_element(by=By.XPATH, value='//h5[text()="Interactions"]')
interactions.click()
print('Interactions click')

# Go to Widgets

elements = driver.find_element(by=By.XPATH, value='//div[text()="Widgets"]')
elements.click()
time.sleep(2)
print('Widgets click')

# Go to Data Picker menu point

buttons_menu = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[3]')
buttons_menu.click()
print('Data Picker menu point click')

# Put new date in the date field

new_date = driver.find_element(by=By.XPATH, value='//input[@id="datePickerMonthYearInput"]')

'''
# new_date.clear() тут почему-то не работает и поэтому мы придумали такой "костыль"
for _ in range(10):
    new_date.send_keys(Keys.BACK_SPACE)

time.sleep(3)
new_date.send_keys('06/17/2022')
print('New date is in the field')
time.sleep(3)
new_date.send_keys(Keys.RETURN)
time.sleep(3)

print('Change tha date by replacing it in the field')
'''

# Choose the date from the calendar opened

'''
new_date.click()
time.sleep(3)
date_17 = driver.find_element(by=By.XPATH, value='//div[@aria-label="Choose Friday, March 17th, 2023"]')
time.sleep(3)
date_17.click()
time.sleep(3)
print('Change tha date by clicking on it when calendar opened')
'''

# Choose today's date

'''
new_date.click()
time.sleep(3)
today_date = driver.find_element(by=By.XPATH, value='//div[contains(@class,"react-datepicker__day--today")]') # обращаемся по части названия класса (не ко всему названию)
time.sleep(3)
today_date.click()
print('Choose today date by clicking on it when calendar opened')
'''

# Choose tomorrow's date

'''
new_date.click()
time.sleep(3)

now_date = datetime.datetime.utcnow().strftime("%d") # get current date
date = int(now_date) + 1 # current date + 1 (current date = 2, 2+1 = 3)
time.sleep(3)

s = ''
if date == 1:
    s = 'st'
elif date == 2:
    s = 'nd'
elif date == 3:
    s = 'rd'
else:
    s = 'th'

locator = f'//div[contains(@aria-label,"{date}{s}, 2023")]'
print(f'Locator: {locator}')

tomorrow_date = driver.find_element(by=By.XPATH, value=locator)
tomorrow_date.click()
print('Choose tomorrow date by clicking on it when calendar opened')
'''

# Choose date = [tomorrow's date + 10 days]

new_date.click()
time.sleep(3)
now_date = datetime.datetime.utcnow().strftime('%d')
date = int(now_date) + 10

now_year = datetime.datetime.utcnow().strftime('%Y')
year = int(now_year)

s = ''
if date == 1:
    s = 'st'
elif date == 2:
    s = 'nd'
elif date == 3:
    s = 'rd'
else:
    s = 'th'

locator = f'//div[contains(@aria-label,"{date}{s}, {year}")]'
print(f'Locator: {locator}')

date_plus_10 = driver.find_element(by=By.XPATH, value=locator)
date_plus_10.click()
print('Choose the date = [current date + 10]')
