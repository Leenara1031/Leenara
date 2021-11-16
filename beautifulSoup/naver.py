from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

browser = webdriver.Chrome()
browser.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105')

def naver(result):
    naver_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
    print(naver_url)
    html = urllib.request.urlopen(naver_url)
    soupNaver = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupNaver.find('tbody')
    for naver in tag_tbody.find_all('tr'):
        if len(naver) <= 3:
            break
        naver_td = naver.find_all('td')
        naver_title = naver_td[0].string
        naver_news = naver_td[1].string
        result.append([naver_title] + [naver_news])

    return

def main():
    result = []
    print('NAVER NEWS CRAWLING')
    naver(result)
    naver_tbl = pd.DataFrame(result, columns= ('title', 'news'))
    naver_tbl.to_csv('./project/naver.csv', encoding='cp949', mode='w', index=True)
    del result[:]

if __name__ == '__main__':
    main()




