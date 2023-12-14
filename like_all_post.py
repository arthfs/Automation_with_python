
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()

session = WebDriver()
session.get("https://www.instagram.com/")

time.sleep(5)

usr=session.find_element(By.NAME,"username")
usr.send_keys(os.getenv('usr'))

passw=session.find_element(By.NAME,"password")
passw.send_keys(os.getenv('passw'))

time.sleep(5)
submit =session.find_element(By.CSS_SELECTOR ,"#loginForm > div > div:nth-child(3) > button > div")
submit.click()


time.sleep(5)
profile= "https://www.instagram.com/ali_plusplus/"
session.get(profile)
time.sleep(7)
post = session.find_element(By.CSS_SELECTOR ,'li.xl565be:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
numpost = int(post.text)

if numpost > 0:
    #if the user has at least one post
    first = session.find_element(By.CSS_SELECTOR,'div._ac7v:nth-child(1) > div:nth-child(1)')
    first.click()
    for i in range (numpost):
        #iterate through all posts
        time.sleep(4)
        
        like = session.find_element(By.CSS_SELECTOR ,'._aamw > div:nth-child(1) > div:nth-child(1)')
        status = like.find_element(By.TAG_NAME,'svg')
        label = status.get_attribute('aria-label')
        
        #verify if we liked the post before
        if label =='Like':
            like.click()
        
        #go to the next post
        next = session.find_element(By.CLASS_NAME,'_abl-')
        next.send_keys(Keys.ARROW_RIGHT)
    
            
        
            