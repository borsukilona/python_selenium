from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

# Get lists with products names and products prices

elements_names = driver.find_elements(by=By.XPATH, value='//div[@class="inventory_item"]//div[@class="inventory_item_name"]')
elements_prices = driver.find_elements(by=By.XPATH, value='//div[@class="inventory_item"]//div[@class="inventory_item_price"]')

product_names = [elements_names[i].text for i in range(len(elements_names))]
product_prices = [elements_prices[i].text for i in range(len(elements_prices))]

# Welcome message

print('Welcome to our internet store')
print(f'Choose one of the following products and input the number: '
      f'\n 1 - {product_names[0]} ({product_prices[0]})'
      f'\n 2 - {product_names[1]} ({product_prices[1]})'
      f'\n 3 - {product_names[2]} ({product_prices[2]})'
      f'\n 4 - {product_names[3]} ({product_prices[3]})'
      f'\n 5 - {product_names[4]} ({product_prices[4]})'
      f'\n 6 - {product_names[5]} ({product_prices[5]})')
product_number = int(input())
print(f'Chosen product is number {product_number}: {product_names[product_number-1]} ({product_prices[product_number-1]})')

# Steps


def info_product(product_n):
    value_product_name = product_names[product_n-1]
    value_product_price = product_prices[product_n-1]
    return value_product_name, value_product_price


def select_product(product_n):
    add_to_card_button = driver.find_element(by=By.XPATH, value=f'//div[@class="inventory_item"][{product_n}]//div[@class="pricebar"]//button')
    add_to_card_button.click()
    print(f"{product_names[product_n-1]} in the cart")


def go_to_cart():
    cart = driver.find_element(by=By.XPATH, value='//a[@class="shopping_cart_link"]')
    cart.click()
    print("Cart is opened")


def info_product_from_cart():
    value_product_cart_name = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_name"]').text
    value_product_cart_price = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_price"]').text
    return value_product_cart_name, value_product_cart_price


def checkout_click():
    checkout = driver.find_element(by=By.XPATH, value='//button[@id="checkout"]')
    checkout.click()
    print("Checkout clicked")


def fill_checkout_form(name, surname, zip):
    first_name = driver.find_element(by=By.XPATH, value='//input[@id="first-name"]')
    first_name.send_keys(name)
    print("Input first name")
    last_name = driver.find_element(by=By.XPATH, value='//input[@id="last-name"]')
    last_name.send_keys(surname)
    print("Input last name")
    postal_code = driver.find_element(by=By.XPATH, value='//input[@id="postal-code"]')
    postal_code.send_keys(zip)
    print("Input zip/postal code")


def submit_checkout():
    continue_button = driver.find_element(by=By.XPATH, value='//input[@id="continue"]')
    continue_button.click()
    print("Continue clicked")


def info_product_overview():
    value_product_overview_name = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_name"]').text
    value_product_overview_price = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_price"]').text
    return value_product_overview_name, value_product_overview_price


def find_total_price():
    total = driver.find_element(by=By.XPATH, value='//div[@class="summary_subtotal_label"]').text
    total_price = total.split()[2]
    print(f'Total price is {total_price}')
    return total_price


def test_compare():
    name_price_products = info_product(product_number)
    name_price_cart = info_product_from_cart()
    name_price_overview = info_product_overview()
    total_price = find_total_price()

    if name_price_products[0] == name_price_cart[0]:
        message = '---Product name from Products == Product name from Cart PASSED---'
        print(message)
        if name_price_products[0] == name_price_overview[0]:
            message = '---Product name from Products == Product name from Overview PASSED---'
            print(message)
    else:
        message = '---FAILED---'
        print(message)

    # --------------------------------------------------

    if name_price_overview[1] == name_price_cart[1]:
        message = '---Product price from Products == Product price from Cart PASSED---'
        print(message)
        if name_price_overview[1] == name_price_overview[1]:
            message = '---Product price from Products == Product price from Overview PASSED---'
            print(message)
    else:
        message = '---FAILED---'
        print(message)

    # --------------------------------------------------

    if name_price_products == name_price_cart == name_price_overview:
        message = '---All the values are equal as expected TEST PASSED---'
        print(message)
    else:
        message = '---FAILED---'
        print(message)

    # --------------------------------------------------

    if total_price == name_price_products[1] == name_price_cart[1] == name_price_overview[1]:
        message = '---Total price is correct TEST PASSED---'
        print(message)
    else:
        message = '---FAILED---'
        print(message)


# Perform the steps

print(f"Selected product info: {info_product(product_number)}")
select_product(product_number)
go_to_cart()
print(f"Selected product info in the cart: {info_product_from_cart()}")
checkout_click()
fill_checkout_form('Ilona', 'Borsuk', '220047')
submit_checkout()
print(f"Selected product info in overview: {info_product_overview()}")
find_total_price()
test_compare()


