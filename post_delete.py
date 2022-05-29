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

email.send_keys("*******.test@gmail.com")
password.send_keys("a*********123")

try:
    profile = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a/div[1]/img')
    profile.click()
except:
    print("there is no profile button!")

try:
    questions = driver.find_element_by_xpath('//*[@id="mainbar-full"]/div[4]/nav/ul/li[3]/a')
    questions.click()
except:
    print("there is no questions button")

try:
    my_question = driver.find_element_by_xpath('//*[@id="question-summary-72252646"]/div[2]/h3/a')
    my_question.click()
except:
    print("there were not found any questions")

try:
    delete_button = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/div[3]/button')
    delete_button.click()
except:
    print("there is no delete button")
