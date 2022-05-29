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
    question_button = driver.find_element_by_xpath('//*[@id="nav-questions"]/span')
    question_button.click()
except:
    print("there is no question button")

try:
    filter_button = driver.find_element_by_xpath('//*[@id="mainbar"]/div[2]/div/div[2]/div/div[3]/button')
    filter_button.click()
except:
    print("there is no filter button in this page")

try:
    click1 = driver.find_element_by_xpath('//*[@id="c3c053f8-574b-49c6-a9dc-d61add0a3ce4"]')
    click2 = driver.find_element_by_xpath('//*[@id="d79496ed-0dbb-4181-a927-00ab0c023758"]')
    click1.click()
    click2.click()
except:
    print("there is no options for filtering")

try: 
    tagged_display = driver.find_element_by_xpath('//*[@id="uql-form"]/div/div/div[1]/div/div[3]/div/div/input')
    tagged_display.send_keys("python")
    click_spawn = driver.find_element_by_xpath('//*[@id="uql-form"]/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/span')
    click_spawn.click()
except:
    print("there is no display for tagged")

try:
    apply_filter = driver.find_element_by_xpath('//*[@id="uql-form"]/div/div/div[2]/div/div[1]/button[1]')
    apply_filter.click()
except:
    print("there is no apply button!")

try:
    select_question = driver.find_element_by_xpath('//*[@id="question-summary-72263534"]/div[2]/h3/a')
    select_question.click()
except:
    print("there was not found any question")

try:
    dislike_button = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[1]/div/button[2]/svg/path')
    dislike_button.click()
except:
    print("there is no dislike button")

try:
    like_button = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[1]/div/button[1]/svg/path')
    like_button.click()
except:
    print("there is no like button")
    