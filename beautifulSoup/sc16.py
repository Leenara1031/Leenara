from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# #01 chrome 검색 자동화
# browser = webdriver.Chrome()
# url = 'https://www.google.co.kr/'
# browser.get(url)                #step01 : 사이트접속
#
# #class 이름 gLFyf                #step02 : element 찾기
# inputs = browser.find_elements(By.CLASS_NAME, 'gLFyf')
# print(f'inputs: {inputs}')
#
# inputs[0].send_keys('python')   #step03 : input search word in input
# inputs[0].send_keys(Keys.ENTER) #step04 : input key(enter) command

# #02 naver.com login 자동화
# browser = webdriver.Chrome()
# browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
#
# #id, pw
# idForInput = browser.find_element(By.ID, 'id')
# idForInput.send_keys('dlskfk42')
#
# pwForInput = browser.find_element(By.ID, 'pw')
# pwForInput.send_keys('0000')
#
# #log.login
# loginBtn = browser.find_element(By.ID, 'log.login')
# loginBtn.click()

#03 gmarket goods search
browser = webdriver.Chrome()
browser.get('https://www.gmarket.co.kr/')

#name = keyword
searchInput = browser.find_element(By.NAME, 'keyword')
searchInput.send_keys('나이키운동화')
# searchInput.send_keys(Keys.ENTER)

#class = image
searchBtn = browser.find_element(By.CLASS_NAME, 'image')
searchBtn.click()

#시간 끌기
#browser.implicitly_wait(2)
#time.sleep(2)

# #신발 이름들
# shoesNameSelector = '#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item'
# shoesNames = browser.find_elements(By.CSS_SELECTOR, shoesNameSelector)
#
# for idx, shoesName in enumerate(shoesNames):
#     print(f'idx: {idx}, \t shoesName: {shoesName.text}')
#
# #신발 가격들
# shoesPriceSelector = '#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong'
# shoesPrices = browser.find_elements(By.CSS_SELECTOR, shoesPriceSelector)
#
# for idx, shoesPrice in enumerate(shoesPrices):
#     print(f'idx: {idx}, \t shoesPrice: {shoesPrice.text}')

# # #go 2page
# pageSelector = '#section__inner-content-body-container > div:nth-child(7) > div > a:nth-child(4)'
# pageNavigator = browser.find_element(By.CSS_SELECTOR, pageSelector)
# pageNavigator.click()
#
# browser.implicitly_wait(2)
#
# #go 3page
# pageSelector = '#section__inner-content-body-container > div:nth-child(3) > div > a:nth-child(5)'
# pageNavigator = browser.find_element(By.CSS_SELECTOR, pageSelector)
# pageNavigator.click()
#
# time.sleep(2)

# browser.close()

#01 5page까지 데이터(신발 이름과 신발 가격)엑셀에 저장해보자!
##section__inner-content-body-container > div:nth-child(3) > div > a:nth-child(7)
