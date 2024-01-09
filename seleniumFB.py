from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pickle

import bs4
import requests
import request
'''
try:
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
except:
    pass
'''
opt = Options()
opt.add_argument('--disable-notifications')
useragent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
opt.add_argument(useragent)
driver = webdriver.Chrome(chrome_options=opt, executable_path='chromedriver.exe')
s = driver.get('https://fb.com')
'''
try:
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
except:
    pass
'''
s = driver.find_element_by_name('email')
s.send_keys('01949411760')
s = driver.find_element_by_name('pass')
s.send_keys('shuvo4025')
s = driver.find_element_by_id('u_0_b')
driver.implicitly_wait(1)
s.send_keys(Keys.RETURN)
time.sleep(1)
#driver.implicitly_wait(7)
#s = driver.find_element_by_id('mount_0_0').find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div').click()
time.sleep(1)
s = driver.get('https://www.facebook.com/groups/naseehah/members')
time.sleep(1)

#try:
#    s = driver.find_elements_by_xpath(
#   f'//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[8]/div/div[2]/div/div[{i}]/div/div/div[2]/div[1]/div/div/div[1]/span/span/div/a')



SCROLL_PAUSE_TIME = 4

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
sss = time.time()
while True:
    # Scroll down to bottom
    if int(sss)+600 < int(time.time()):
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
y = []
yy = open('mylinks.txt', 'w')
for i in range(1, 3000):
   #s = driver.find_elements_by_xpath(f'//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[8]/div/div[2]/div/div[{i}]/div/div/div[1]/span/div/a')
   s = driver.find_elements_by_xpath(
       f'//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[15]/div/div[2]/div/div[{i}]/div/div/div[2]/div[1]/div/div/div[1]/span/span/div/a')

   for w in s:
      w = w.get_attribute('href')
      print(w)
      yy.write(w+'\n')
      y.append(w)

#s.find_element('data-visualcompletion', 'ignore-dynamic')

print(len(y))
#//*[@id="u_0_1z"]/div[2]/div[8]
#//*[@id="recently_joined_100048624245416"]
#

#s = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]')
#s = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]').
#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/span
##################################//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]
#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div
#s = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]')
#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]
#/div/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[8]/div/div[2]
#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]
#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[8]/div/div[2]
#s = driver.find_element_by_id('mount_0_0').find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[10]/a').click()
#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[10]/a
#//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div
#//*[@id="mount_0_0"]/div/div/div[1]/div[2]
#s = driver.find_element_by_xpath("//div[@class='n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3']")
##s = driver.find_element_by_class_name('a8c37x1j ms05siws hwsy1cff b7h9ocf4 em6zcovv').click()
#s = driver.find_element_by_class_name('oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql jq4qci2q a3bd9o3v lrazzd5p oo9gr5id').click()
