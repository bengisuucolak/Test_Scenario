from distutils.command.upload import upload
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/users/login?ssrc=head")
driver.implicitly_wait(8)

try:
    my_element = driver.find_element_by_id("submit-button")
    my_element.click()
except:
    print("there is no email and password")

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email.send_keys("andromeda.2022.test@gmail.com")
password.send_keys("andromeda123")

try:
    profile = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a/div[1]/img')
    profile.click()
except:
    print("there is no profile button!")

try:
    edit_profile = driver.find_element_by_xpath('//*[@id="mainbar-full"]/div[1]/div[2]/a')
    edit_profile.click()
except:
    print("There is no edit profile button!")

try:
    display_name = driver.find_element_by_xpath('//*[@id="displayName"]')
    display_name.send_keys("Hello my name is puppet!")
except:
    print("display was not found!")

try:
    save_profile = driver.find_element_by_xpath('//*[@id="form-submit"]/div/button')
    save_profile.click()
except:
    print("there is no button for save the changes")