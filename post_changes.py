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
    edit_button = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/a')
    edit_button.click()
except:
    print("there is no edit button")

try:
    add_comment = driver.find_element_by_xpath('//*[@id="comments-link-72252646"]/a[1]')
    add_comment.click()
    add_comment_display = driver.find_element_by_xpath('//*[@id="add-comment-72252646"]/div/div[1]/div/textarea')
    add_comment_display.send_keys("hello everyone, this is a test video")
except:
    print("there is no edit summary display")

try:
    add_button = driver.find_element_by_xpath('//*[@id="add-comment-72252646"]/div/div[2]/div/button[1]')
    add_button.click()
except:
    print("there was not found any add comment button")

try:
    more_body = driver.find_element_by_xpath('//*[@id="wmd-input-72252646"]')
    more_body.send_keys(" hello everyone, this is a test video for my project")
except:
    print("there was not found the display")

try:
    save_button = driver.find_element_by_xpath('//*[@id="submit-button"]')
    save_button.click()
except:
    print("there is no save button")