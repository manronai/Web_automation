#hr@intellipaat.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.chrome.options import Options

opts = Options()

opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36")

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'
s = driver.get(url=url)
s = driver.find_element_by_xpath('//*[@id="firstName"]').send_keys('gachh')
s = driver.find_element_by_xpath('//*[@id="lastName"]').send_keys('pala')
s = driver.find_element_by_xpath('//*[@id="username"]').send_keys('gachhpala1')
s = driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys('gachhpala111#')
s = driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
s.send_keys('gachhpala111#')
sleep(2)
s.send_keys(Keys.RETURN)
sleep(2)
s = driver.find_element_by_xpath('//*[@id="phoneNumberId"]')
s.send_keys('+19124216431')
s.send_keys(Keys.RETURN)
s = input()
if s:
    s = driver.find_element_by_xpath('')
    s.send_keys(Keys.RETURN)
