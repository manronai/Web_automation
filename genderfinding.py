from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from test import ch
import time
import bs4
import requests
import request
nogender = open('nogender.txt', 'w')
female = open('female.txt', 'w')
male = open('male.txt', 'w')
opt = Options()
opt.add_argument('--disable-notifications')
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
driver = webdriver.Chrome(chrome_options=opt, executable_path='chromedriver.exe')
s = driver.get('https://fb.com')
s = driver.find_element_by_name('email')
s.send_keys('01949411760')
s = driver.find_element_by_name('pass')
s.send_keys('shuvo4025')
time.sleep(3)
s.send_keys(Keys.RETURN)
time.sleep(2)
filename = open('mylinks.txt')
for t in filename:
    time.sleep(1)
    c = ch.Link(t)
    try:
        s = driver.get(c)
        time.sleep(1)
        s = driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]/span')
        ss = s.text
        if str(ss) == 'Female':
            female.write(c + '\n')
        elif str(ss) == 'Male':
            male.write(c + '\n')


    except:
        time.sleep(1)
        nogender.write(c + '\n')

    print(c)



