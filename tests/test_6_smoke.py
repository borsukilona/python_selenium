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

'''
Info product 1 (Products page)
'''

product_1 = driver.find_element(by=By.XPATH, value='//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1) # Sauce Labs Backpack

product_1_price = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_product_1_price = product_1_price.text
print(value_product_1_price) # $29.99

'''
Add product 1 to the cart
'''

select_product_1 = driver.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Product in the cart")

'''
Go to the cart
'''

cart = driver.find_element(by=By.XPATH, value='//a[@class="shopping_cart_link"]')
cart.click()
print("Cart is opened")

'''
Info product 1 from the cart
'''

cart_product_1 = driver.find_element(by=By.XPATH, value='//a[@id="item_4_title_link"]')
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1) # Sauce Labs Backpack

assert value_product_1 == cart_value_product_1, "Product name from Products doesn't correspond to the product name from the cart"
print("---Name Product == Name Cart PASSED---")

cart_product_1_price = driver.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
cart_value_product_1_price = cart_product_1_price.text
print(cart_value_product_1_price) # $29.99

assert value_product_1_price == cart_value_product_1_price, "Product price from Products doesn't correspond to the product price from the cart"
print("---Price Product == Price Cart PASSED---")

'''
Checkout 
'''

checkout = driver.find_element(by=By.XPATH, value='//button[@id="checkout"]')
checkout.click()
print("Checkout clicked")

'''
Fill in the checkout form (Your Information) 
'''

first_name = driver.find_element(by=By.XPATH, value='//input[@id="first-name"]')
first_name.send_keys("Ilona")
print("Input first name")
last_name = driver.find_element(by=By.XPATH, value='//input[@id="last-name"]')
last_name.send_keys("Borsuk")
print("Input last name")
postal_code = driver.find_element(by=By.XPATH, value='//input[@id="postal-code"]')
postal_code.send_keys("220047")
print("Input zip/postal code")

'''
Continue after filling the checkout info
'''

continue_button = driver.find_element(by=By.XPATH, value='//input[@id="continue"]')
continue_button.click()
print("Continue clicked")

'''
Info product 1 from overview after making checkout before finishing the process
'''

overview_product_1 = driver.find_element(by=By.XPATH, value='//a[@id="item_4_title_link"]')
overview_value_product_1 = overview_product_1.text
print(overview_value_product_1) # Sauce Labs Backpack

assert overview_value_product_1 == cart_value_product_1, "Product name from cart doesn't correspond to the product name from the overview"
print("---Name Cart == Name Overview PASSED---")

overview_product_1_price = driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
overview_value_product_1_price = overview_product_1_price.text
print(overview_value_product_1_price) # $29.99

assert overview_value_product_1_price == cart_value_product_1_price, "Product price from Cart doesn't correspond to the product price from the overview"
print("---Price Cart == Price Overview PASSED---")

'''
Check the total price
'''

total_sum = driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_total_sum = total_sum.text
print(value_total_sum)


assert value_total_sum.split()[2] == cart_value_product_1_price, "Product price from Cart doesn't correspond to the total sum"
print("---Price Cart == Total sum PASSED---")

'''
Check if the info about the product is the same in the overview, in the cart and in the products page
'''

if (value_product_1 == cart_value_product_1 == overview_value_product_1) and \
        (value_product_1_price == cart_value_product_1_price == overview_value_product_1_price == value_total_sum.split()[2]):
    print("---TEST PASSED---")
else:
    print("---FAILED---")

