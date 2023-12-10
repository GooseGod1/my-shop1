### Отоброжение страницы товара
import time

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# My_account = driver.find_element_by_css_selector('#menu-item-50 a')
# My_account.click()
# Username = driver.find_element_by_id("username")
# Username.send_keys("guzyak2000@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("123F321e.")
# Login = driver.find_element_by_name("login")
# Login.click()
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# Html_book = driver.find_element_by_css_selector("[alt='Mastering HTML5 Forms']")
# Html_book.click()
# element = driver.find_element_by_css_selector("[itemprop='name']")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"
# driver.quit()

### Кол-во товаров в категории

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# My_account = driver.find_element_by_css_selector('#menu-item-50 a')
# My_account.click()
# Username = driver.find_element_by_id("username")
# Username.send_keys("guzyak2000@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("123F321e.")
# Login = driver.find_element_by_name("login")
# Login.click()
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# Html = driver.find_element_by_css_selector("#woocommerce_product_categories-2 li:nth-child(2) a")
# Html.click()
# items = driver.find_elements_by_class_name("size-shop_catalog")
# if len(items) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items)))
# driver.qfrom selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# My_account = driver.find_element_by_css_selector('#menu-item-50 a')
# My_account.click()
# Username = driver.find_element_by_id("username")
# Username.send_keys("guzyak2000@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("123F321e.")
# Login = driver.find_element_by_name("login")
# Login.click()
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# Html = driver.find_element_by_css_selector("#woocommerce_product_categories-2 li:nth-child(2) a")
# Html.click()
# items = driver.find_elements_by_class_name("size-shop_catalog")
# if len(items) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items)))
# driver.quit()

### Сортировка товаров

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# My_account = driver.find_element_by_css_selector('#menu-item-50 a')
# My_account.click()
# Username = driver.find_element_by_id("username")
# Username.send_keys("guzyak2000@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("123F321e.")
# Login = driver.find_element_by_name("login")
# Login.click()
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# element = driver.find_element_by_class_name("orderby")
# element_check = element.get_attribute("value")
# assert element_check == "menu_order"
# Select = driver.find_element_by_class_name("orderby")
# Select.click()
# High_to_low = driver.find_element_by_css_selector("select > option:nth-child(6)")
# High_to_low.click()
# element = driver.find_element_by_class_name("orderby")
# element_check = element.get_attribute("value")
# assert element_check == "price-desc"
# driver.quit()

### Отображение, скидка товара

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# My_account = driver.find_element_by_css_selector('#menu-item-50 a')
# My_account.click()
# Username = driver.find_element_by_id("username")
# Username.send_keys("guzyak2000@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("123F321e.")
# Login = driver.find_element_by_name("login")
# Login.click()
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# Android = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']")
# Android.click()
# element = driver.find_element_by_css_selector("del .amount")
# element_get_text = element.text
# assert element_get_text == "₹600.00"
# element = driver.find_element_by_css_selector("ins .amount")
# element_get_text = element.text
# assert element_get_text == "₹450.00"
# Photo = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='Android Quick Start Guide']")) )
# Photo.click()
# Close = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
# Close.click()
# driver.quit()

### Проверка цены в корзине

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# Books = driver.find_element_by_css_selector("[data-product_id='182']")
# Books.click()
# time.sleep(3)
# element = driver.find_element_by_class_name("wpmenucart-contents")
# element_get_text = element.text
# assert element_get_text == "1 Item₹180.00"
# Basket = driver.find_element_by_class_name("wpmenucart-contents")
# Basket.click()
# Subtotal = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] > span"), "₹180.00"))
# Total = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong > span"), "₹183.60"))
# driver.quit()

### Работа в корзине

# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# Shop_btn.click()
# driver.execute_script("window.scrollBy(0,300)","")
# One_book = driver.find_element_by_css_selector("[data-product_id='182']")
# One_book.click()
# time.sleep(1)
# Second_Book = driver.find_element_by_css_selector("[data-product_id='180']")
# Second_Book.click()
# time.sleep(1)
# Basket = driver.find_element_by_class_name("wpmenucart-contents")
# Basket.click()
# time.sleep(1)
# Delete_one = driver.find_element_by_css_selector("[data-product_id='182']")
# Delete_one.click()
# Undo = driver.find_element_by_css_selector(".woocommerce-message > a")
# Undo.click()
# Quantity = driver.find_element_by_css_selector("tr:nth-child(1) [value='1']")
# Quantity.clear()
# Quantity.send_keys("3")
# Update_btn = driver.find_element_by_css_selector("[name='update_cart']")
# Update_btn.click()
# element = driver.find_element_by_css_selector("tr:nth-child(1) [type='number']")
# element_check = element.get_attribute("value")
# assert element_check == "3"
# time.sleep(1)
# Apply_btn = driver.find_element_by_css_selector("[name='apply_coupon']")
# Apply_btn.click()
# element = driver.find_element_by_css_selector(".woocommerce-error > li")
# element_get_text = element.text
# assert element_get_text == "Please enter a coupon code."
# driver.quit()

#### Покупка товара

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://practice.automationtesting.in/')
Shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
Shop_btn.click()
driver.execute_script("window.scrollBy(0,300)","")
Books = driver.find_element_by_css_selector("[data-product_id='182']")
Books.click()
time.sleep(1)
Basket = driver.find_element_by_class_name("wpmenucart-contents")
Basket.click()
Proceed_btn = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a")) )
Proceed_btn.click()
First_name = driver.find_element_by_id("billing_first_name")
First_name.send_keys("Сергей")
Last_name = driver.find_element_by_id("billing_last_name")
Last_name.send_keys("Гусь")
Email = driver.find_element_by_id("billing_email")
Email.send_keys("guzyak2000@mail.ru")
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("99123332314")
Country = driver.find_element_by_id("s2id_billing_country")
Country.click()
Country_Russia = driver.find_element_by_id("s2id_autogen1_search")
Country_Russia.send_keys("Russia")
Russia = driver.find_element_by_css_selector("ul > li > .select2-result-label")
Russia.click()
Address = driver.find_element_by_id("billing_address_1")
Address.send_keys("ул. Имени Криворуких д.52")
Apartment = driver.find_element_by_id("billing_address_2")
Apartment.send_keys("23")
City = driver.find_element_by_id("billing_city")
City.send_keys("Омск")
State = driver.find_element_by_id("billing_state")
State.send_keys("Варшавское")
Postcode = driver.find_element_by_id("billing_postcode")
Postcode.send_keys("01232")
driver.execute_script("window.scrollBy(0,600)","")
time.sleep(3)
Payments = driver.find_element_by_id("payment_method_cheque")
Payments.click()
Place_order = driver.find_element_by_id("place_order")
Place_order.click()
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3)"), "Check Payments"))
driver.quit()


