from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib import request as rq

url = 'https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl'

browser = webdriver.Chrome()
browser.get(url)

#class = gLFyf gsfi
searchInput = browser.find_element(By.CLASS_NAME, 'gLFyf')
searchInput.send_keys('BTS')
searchInput.send_keys(Keys.ENTER)

time.sleep(2)

endHeight = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

    currentHeight = browser.execute_script('return document.body.scrollHeight')
    if currentHeight == endHeight:
        try:
            moreBtn = browser.find_element(By.CLASS_NAME, 'mye4qd')
            moreBtn.click()

        except Exception as e:
            print(e)
            break

    endHeight = currentHeight

thums = browser.find_elements(By.CLASS_NAME, 'Q4LuWd')
print(f'thums length: {len(thums)}')

browser.execute_script('window.scrollTo(0, 0)')
for idx, thum in enumerate(thums):

    try:
        thum.click()

        time.sleep(1)
        oriImgURL = browser.find_element(By.CLASS_NAME, 'n3VNCb').get_attribute('src')
        rq.urlretrieve(oriImgURL, 'C:/lnr_scraping/download/img/testImg' + str(idx) + '.jpg')

    except Exception as e:
        print(e)

browser.close()