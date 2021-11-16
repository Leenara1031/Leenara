from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import effectiveModule

browser = webdriver.Chrome()
browser.get('https://finance.naver.com/sise/lastsearch2.naver')

# [3, 4, 5, 6, 7,
# 11, 12, 13, 14, 15,
# 19, 20, 21, 22, 23,
# 27, 28, 29, 30, 31,
# 35, 36, 37, 38, 39,
# 43, 44, 45, 46, 47]

eTrs = effectiveModule.getEffectibeTrs()
print(eTrs)

while True:
    for i in range(len(eTrs)):
        searchSelector = '#contentarea > div.box_type_l > table > tbody > tr:nth-child({trNum}) > td.no'
        searchSelector = searchSelector.format(trNum = eTrs[i])
        print(f'searchSelector: {searchSelector}')
        searchInput = browser.find_element(By.CSS_SELECTOR, searchSelector)
        print(f'순위: {searchInput.text}')

        searchSelector = '#contentarea > div.box_type_l > table > tbody > tr:nth-child({trNum}) > td:nth-child(2) > a'
        searchSelector = searchSelector.format(trNum = eTrs[i])
        searchInput = browser.find_element(By.CSS_SELECTOR, searchSelector)
        print(f'종목명: {searchInput.text}')

    time.sleep(60*10)
    browser.refresh()

browser.close()