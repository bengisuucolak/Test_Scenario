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
    question_s = driver.find_element_by_xpath('//*[@id="nav-questions"]/span')
    question_s.click()
except:
    print("there is no clickable question!")

try:
    edit_button = driver.find_element_by_class_name("wmd-input s-input bar0 js-post-body-field processed")
    edit_button.click()
except:
    print("there is no edit button!")

try:
    answer_question = driver.find_element_by_xpath('//*[@id="wmd-input"]')
    answer_question.send_keys("this is a test answer.")
except:
    print("there is no answer comment!")

try:
    save_button = driver.find_element_by_id("submit-button")
    save_button.click()
except:
    print("there is no save button!")