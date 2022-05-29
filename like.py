from cmath import exp
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
    question_go = driver.find_element_by_xpath('//*[@id="question-summary-72264170"]/div[2]/h3/a')
    question_go.click()
except:
    print("there is no question")


try:
    like_button = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[1]/div/button[1]')
    like_button.click()
except:
    print("there is no like button")

