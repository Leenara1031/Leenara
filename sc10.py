from urllib import request as rq
from bs4 import BeautifulSoup as bs
import time

# 데이터 가져오기
url = 'https://www.naver.com/'
naverData = rq.urlopen(url).read()
naverText = naverData.decode('UTF-8')

print(f'naverText: {naverText}')

# 데이터 분석하기
soup = bs(naverText, 'html.parser')
aTags = soup.find_all('a')

for idx, ele in enumerate(aTags):
    print(f'idx: {idx}, \t eleStr: {ele.string}, \t href: {ele.attrs["href"]}')
#
# for a in aTags:
#     print(f'a: {a.string}')
#
# def getCurrentTime():
#     return time.srtftime('[%Y-%m-%d %H:%M:%S]')
#
# def converIntToStr(idx):
#     return '[' + str(idx) + ']'
#
# for idx, ele in enumerate(aTags):
#     with open('C:/lnr_scraping/download/naverA.txt/', 'a') as f:
#         f.write(f'{getCurrentTime()} {converIntToStr(idx)} {ele.string}\n')