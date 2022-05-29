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
password.send_keys("a**********123")

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
    change_photo = driver.find_element_by_xpath('//*[@id="change-picture"]')
    change_photo.click()
except:
    print("There is no change photo button!")

try:
    upload_photo = driver.find_element_by_xpath('//*[@id="avatar-upload"]')
    upload_photo.click()
except:
    print("there is no upload photo button!")

try:
    click_for_upload = driver.find_element_by_xpath('/html/body/div[10]/form/div[1]/div[1]/div[1]')
    change_link = driver.find_element_by_xpath('/html/body/div[10]/form/div[1]/div[2]/div[1]/a')
    change_link.click()
except:
    print("there is no button for upload!")

try:
    find_link_line = driver.find_element_by_xpath('/html/body/div[10]/form/div[1]/div[2]/div[2]/input')
    find_link_line.send_keys('https://theconversation.com/physics-and-psychology-of-cats-an-improbable-conversation-176020')
    
except:
    print("the picture was not found")
    
try:    
    change_pic = driver.find_element_by_xpath('/html/body/div[10]/form/div[2]/div[1]/button')
    change_pic.click()
except:
    print("the button was not found")

try:
    save_profile = driver.find_element_by_xpath('//*[@id="form-submit"]/div/button')
    save_profile.click()
except:
    print("there is no save profile button")

