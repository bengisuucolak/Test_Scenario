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

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email.send_keys("andromeda.2022.test@gmail.com")
password.send_keys("andromeda123")

try:
    ask_element = driver.find_element_by_xpath("//*[@id='mainbar']/div[1]/div/a")
    ask_element.click()
except:
    print("there is no button!")

try:
    question_title = driver.find_element_by_xpath("//*[@id='title']")
    question_body = driver.find_element_by_xpath("//*[@id='wmd-input']")
    question_tag = driver.find_element_by_xpath('//*[@id="tageditor-replacing-tagnames--input"]')

    question_title.send_keys("How can i test with selenium?")
    question_body.send_keys("** I am just trying selenium codes for my homework. 
                This question is a part of the test. Please do not answer this question. Thank you for your interest. **")
    question_tag.send_keys("selenium")

    question_tag_click = driver.find_element_by_xpath('//*[@id="tag-editor"]/div[1]/div/div[2]/div[1]/div[2]/div[1]/p')
    question_tag_click.click()
    question_button = driver.find_element_by_xpath('//*[@id="post-form"]/div[2]/div/button[1]')
    question_button.click()
    post_button = driver.find_element_by_class_name("submit-button")
    post_button.click()
except:

    print("there is no question button!")


