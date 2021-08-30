from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.bestbuy.com/site/returnal-standard-edition-playstation-5/6430755.p?skuId=6430755')

buyButton = False
while not buyButton:

    try:
        #check if the button existgs
        addToCartBtn = addButton = driver.find_element_by_class_name("btn-disabled")
        #report status
        print("coming soon")
        #refresh sequence
        time.sleep(1)
        driver.refresh()

    except:
        #button updates to desired state
        addToCartBtn = addButton = driver.find_element_by_class_name("add-to-cart-button")
        #Click the button
        print("Attempting button click")
        addToCartBtn.click()


        #Go to Cart
        driver.get("https://www.bestbuy.com/cart")
        #initiate checkout
        checkoutBtn = buyButton = driver.find_element_by_class_name("checkout-buttons_checkout")
        time.sleep(3)
        checkoutBtn.click()


