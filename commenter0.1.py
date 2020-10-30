import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
file = open('users.txt','r')
names = []
for i in file:
    names.append(i)
for i in range(1):
    file.close()
    driver.get('https://www.aparat.com/signin')
    time.sleep(3)
    username = driver.find_element_by_id('username')
    username.send_keys(str(names[i]))
    time.sleep(1)
    time.sleep(2)
    password = driver.find_element_by_id('password')
    password.clear()
    password.send_keys('Here you write your password'+Keys.ENTER)
    time.sleep(5)
    driver.get('https://www.aparat.com/v/0UELA')
    time.sleep(3)
    followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
    if followvalid.text =='دنبال کردن':
        driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
        driver.delete_all_cookies()
    else:
        driver.delete_all_cookies()
for i in range(95,201):
    number = open('')
    driver.get('https://www.aparat.com/signin')
    time.sleep(3)
    username = driver.find_element_by_id('username')
    username.send_keys(str(names[i]))
    driver.find_element_by_xpath('//*[@id="main-container"]/section/div/div[2]/form/button').click()
    time.sleep(1)
    time.sleep(2)
    password = driver.find_element_by_id('password')
    password.clear()
    password.send_keys('Here you write your password'+Keys.ENTER)
    time.sleep(5)
    driver.get('https://www.aparat.com/v/0UELA')
    time.sleep(3)
    followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
    if followvalid.text =='دنبال کردن':
        driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
        driver.delete_all_cookies()
    else:
        driver.delete_all_cookies()
