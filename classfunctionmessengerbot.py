from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import bs4
import requests
import request
opt = Options()
opt.add_argument('--disable-notifications')
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
opt.add_argument('useragent='+useragent)
driver = webdriver.Chrome(chrome_options=opt, executable_path='chromedriver.exe')
s = driver.get('https://fb.com')
def forpaANDem(em, pa):
    s = driver.find_element_by_name('email')
    s.send_keys(em)
    s = driver.find_element_by_name('pass')
    s.send_keys(pa)
    s = driver.find_element_by_id('u_0_b')
    driver.implicitly_wait(3)
    s.send_keys(Keys.RETURN)
    time.sleep(2)
def outsidefileAndID(idlin, texts):
    #driver.implicitly_wait(7)
    #s = driver.find_element_by_id('mount_0_0').find_element_by_xpath(
        #'//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div').click()
    #driver.implicitly_wait(6)
    time.sleep(3)
    s = driver.get(idlin)
    SCROLL_PAUSE_TIME = 3
    time.sleep(3)
    try:
        s = driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/span').click()
        try:
            driver.find_element_by_xpath(
                '//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[2]').click()
        except:
            pass
        time.sleep(4)
        s = driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div')
        time.sleep(2)
        s.send_keys(texts)
        time.sleep(3)
        s.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div').click()
    except:
        pass

class messengerbot():
    def __init__(self, eml, pas, idlinks, text):
        forpaANDem(eml, pas)
        time.sleep(2)
        f = open(idlinks)
        for i in f:
            print(i)
            time.sleep(3)
            outsidefileAndID(i, text)
    #def fileAndId(self,  idLink):
        #filelines = open(file, 'r')
        #for i in filelines:
m = messengerbot('01949411760', 'shuvo4025', 'mylinks.txt', 'প্রথম থেকে দ্বাদশ শ্রেণীর ছাত্র - ছাত্রীদের দ্রুত সিলেবাস সম্পূর্ণ এবং দ্রুত পরীক্ষার প্রস্তুতির জন্য  শিক্ষক - শিক্ষিকা দেওয়া হয়। অনলাইন এবং অফলাইন আরবি শিক্ষক - শিক্ষিকা দেওয়া হয়। যোগাযোগ ঃ ০১৭৫২৩০৪৬০১')
