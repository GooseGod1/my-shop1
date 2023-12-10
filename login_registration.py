### Регистрация аккаунта
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# My_account = driver.find_element_by_css_selector('#menu-item-50 a')
# My_account.click()
# Email = driver.find_element_by_id("reg_email")
# Email.send_keys("guzyak2000@mail.ru")
# Password = driver.find_element_by_id("reg_password")
# Password.send_keys("123F321e.")
# Register = driver.find_element_by_name("register")
# Register.click()
# driver.quit()

### Вход в систему
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# Logout_element= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li [href='https://practice.automationtesting.in/my-account/customer-logout/']"), "Logout"))
# driver.quit()