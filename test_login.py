from selenium import webdriver
from pages.login_page import LoginPage
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

login = LoginPage(driver)

login.enter_username("standard_user")
login.enter_password("secret_sauce")
login.click_login()

time.sleep(3)
driver.quit()