from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def getKyobobooks(result):
    kyobobooks_URL = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
    browser = webdriver.Chrome('chromedriver.exe')

    browser.get(kyobobooks_URL)
    time.sleep(3)

    eleSelect = Select(browser.find_element(By.ID, 'list_button_wrap'))
    eleSelect.select_by_index(0)
    time.sleep(3)

    booksEle = browser.find_element(By.ID, 'indexCnt')
    booksCnt = booksEle.text

    booksPageCnt = int(booksCnt) / 20
    if booksPageCnt % 10 != 0:
        booksPageCnt = booksPageCnt + 1
    booksPageCnt = int(booksPageCnt)

    print(f'booksPageCnt: {booksPageCnt}')

    for i in range(booksPageCnt):
        nextBtn = browser.find_element(By.CLASS_NAME, 'btn_next')
        browser.execute_script('arguments[0].click()', nextBtn)
        time.sleep(1)

        for j in range(2, 10):

            try:
                bookTitle = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > onclick > title')
                bookAuthor = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span > onclick > author')
                boodReview = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span > onclick > review')
                bookPrice = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span >  book_price')
                print(f'bookTitle: {bookTitle.text}')
                print(f'bookAuthor: {bookAuthor.text}')
                print(f'boodReview: {boodReview.text}')
                print(f'bookPrice: {bookPrice.text}')

            except Exception as e:
                print(e)
                print('no books info!!!')
                break

def main():
    result = []
    getKyobobooks(result)

if __name__ == '__main__':
    main()
