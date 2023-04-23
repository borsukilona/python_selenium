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
Info product 2 (Products page)
'''

product_2 = driver.find_element(by=By.XPATH, value='//a[@id="item_0_title_link"]')
value_product_2 = product_2.text
print(value_product_2) # Sauce Labs Backpack

product_2_price = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_product_2_price = product_2_price.text
print(value_product_2_price) # $9.99

'''
Add product 1 to the cart
'''

select_product_1 = driver.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Product 1 in the cart")

'''
Add product 2 to the cart
'''

select_product_2 = driver.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-bike-light"]')
select_product_2.click()
print("Product 2 in the cart")

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
print(cart_value_product_1)

assert value_product_1 == cart_value_product_1, "Product 1 name from Products doesn't correspond to the product 1 name from the cart"
print("---Name Product 1 == Name Cart 1 PASSED---")

cart_product_1_price = driver.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
cart_value_product_1_price = cart_product_1_price.text
print(cart_value_product_1_price)

assert value_product_1_price == cart_value_product_1_price, "Product 1 price from Products doesn't correspond to the product 1 price from the cart"
print("---Price Product 1 == Price Cart 1 PASSED---")

'''
Info product 2 from the cart
'''

cart_product_2 = driver.find_element(by=By.XPATH, value='//a[@id="item_0_title_link"]')
cart_value_product_2 = cart_product_2.text
print(cart_value_product_2)

assert value_product_2 == cart_value_product_2, "Product 2 name from Products doesn't correspond to the product 2 name from the cart"
print("---Name Product 2 == Name Cart 2 PASSED---")

cart_product_2_price = driver.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
cart_value_product_2_price = cart_product_2_price.text
print(cart_value_product_2_price)

assert value_product_2_price == cart_value_product_2_price, "Product 2 price from Products doesn't correspond to the product 2 price from the cart"
print("---Price Product 2 == Price Cart 2 PASSED---")

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

assert overview_value_product_1 == cart_value_product_1, "Product 1 name from cart doesn't correspond to the product 1 name from the overview"
print("---Name Cart 1 == Name Overview 1 PASSED---")

overview_product_1_price = driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
overview_value_product_1_price = overview_product_1_price.text
print(overview_value_product_1_price) # $29.99

assert overview_value_product_1_price == cart_value_product_1_price, "Product 1 price from Cart doesn't correspond to the product 1 price from the overview"
print("---Price Cart 1 == Price Overview 1 PASSED---")

'''
Info product 2 from overview after making checkout before finishing the process
'''

overview_product_2 = driver.find_element(by=By.XPATH, value='//a[@id="item_0_title_link"]')
overview_value_product_2 = overview_product_2.text
print(overview_value_product_2)

assert overview_value_product_2 == cart_value_product_2, "Product 2 name from cart doesn't correspond to the product 2 name from the overview"
print("---Name Cart 2 == Name Overview 2 PASSED---")

overview_product_2_price = driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
overview_value_product_2_price = overview_product_2_price.text
print(overview_value_product_2_price)

assert overview_value_product_2_price == cart_value_product_2_price, "Product 2 price from Cart doesn't correspond to the product 2 price from the overview"
print("---Price Cart 2 == Price Overview 2 PASSED---")

'''
Find the sum of the products in the cart
'''

cart_sum = float(cart_value_product_1_price.replace('$', '')) + float(cart_value_product_2_price.replace('$', ''))
print(f'Cart sum is {cart_sum}')

'''
Check the total price
'''

total_sum = driver.find_element(by=By.XPATH, value='//div[@class="summary_subtotal_label"]')
value_total_sum = total_sum.text
print(f'Total sum is {value_total_sum.split()[2]}')

assert value_total_sum.split()[2].replace("$", '') == str(cart_sum), "Product price from Cart doesn't correspond to the total sum"
print(f'---{value_total_sum.split()[2].replace("$", "")} == {str(cart_sum)}---')
print("---Price Cart == Total sum PASSED---")



