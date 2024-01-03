import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
from selenium_firefox import Firefox
# driver = Firefox('firefox_profile')
# driver.get('https://google.com')
file = open('users.txt','r')
names = []
counter = 0 
for i in file:
    names.append(i)
    for i in range(1):
        # file.close()
        driver.get('https://www.aparat.com/signin')
        time.sleep(3)
        username = driver.find_element('id','username')
        username.send_keys(str(names[counter]))
        time.sleep(1)
        time.sleep(2)
        driver.find_element('xpath','/html/body/div/main/div/section/div/div[2]/form/button').click()
        time.sleep(5)
        password = driver.find_element('id','password')
        password.clear()
        # here you sopppoe to Enter password for all of your accounts
        
        password.send_keys('1520642814Ghh'+Keys.ENTER)
        time.sleep(5)
        # driver.get('https://www.aparat.com/v/0UELA')
        # here you have to enter you channel link 
        driver.get('https://www.aparat.com/Pyramid.Course')

        time.sleep(8)
        followvalid = driver.find_element('xpath','/html/body/div[2]/main/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/button')
        if followvalid.text =='دنبال کردن':
            driver.find_element('xpath','/html/body/div[2]/main/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/button').click()
            driver.delete_all_cookies()
        else:
            driver.delete_all_cookies()
        counter = counter + 1 
            
            
            
            
# # for i in range(95,201):
#     number = open('')
#     driver.get('https://www.aparat.com/signin')
#     time.sleep(3)
#     username = driver.find_element_by_id('username')
#     username.send_keys(str(names[i]))
#     driver.find_element_by_xpath('//*[@id="main-container"]/section/div/div[2]/form/button').click()
#     time.sleep(1)
#     time.sleep(2)
#     password = driver.find_element_by_id('password')
#     password.clear()
#     password.send_keys('Here you write your password'+Keys.ENTER)
#     time.sleep(5)
#     driver.get('https://www.aparat.com/v/0UELA')
#     time.sleep(3)
#     followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
#     if followvalid.text =='دنبال کردن':
#         driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
#         driver.delete_all_cookies()
#     else:
#         driver.delete_all_cookies()
