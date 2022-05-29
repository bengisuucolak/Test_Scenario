from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/users/login?ssrc=head" )
driver.implicitly_wait(8)

try:
    my_element = driver.find_element_by_id("submit-button")
    my_element.click()
except:
    print("there is no email and password")

try:
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")

    email.send_keys("*********.test?@gmail.com")
    password.send_keys("a************123")
except:
    print("Your email is wrong!")

