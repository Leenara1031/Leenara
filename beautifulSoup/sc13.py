from urllib import request as rq
from urllib import parse as ps
from bs4 import BeautifulSoup as bs
import myUtil
import saveToExcel as s2e

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'

#01 parsameter setting
locationDic = {'stnId':'133'}
params = ps.urlencode(locationDic)
print(f'params : {params}')
url = url + '?' + params
print(f'url : {url}')

#02 data load
urlObj = rq.urlopen(url)
print(f'urlObj : {urlObj}')

#03 test read
urlData = urlObj.read()
print(f'urlData : {urlData}')

#04 data decode
urlText = urlData.decode('UTF-8')
print(f'urlText : {urlText}')

#05 BeautifulSoup
html = '''
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<title>teamHTML document</title>
</head>

<body>

	<div class="top">
	
		<div>top</div>
	
	</div>
	
	<div class="nav">
	
		<div class="menu_wrap">
			<a href="#none">menu01</a> &nbsp;&nbsp;
			<a href="#none">menu02</a> &nbsp;&nbsp;
			<a href="#none">menu03</a> &nbsp;&nbsp;
		</div>
	
	</div>
	
	<div class="section">
	
		<div class="section_wrap">
			<h1>NEWS DESK</h1>
			<p id='news_desk' class='news'>9시 뉴스입니다.</p>
			
			<h2>오늘 주요 뉴스</h2>
			<p id='today_news' class='news'>오늘 뉴스입니다. 드디어 코로나 19가 종식 되었습니다. 마스크 벗으세요.</p>
			
			<h2>오늘 날씨</h2>
			<p id='today_weather' class='news'>간절기 감기조심하세요.</p>
			
			<h2>스포츠 뉴스</h2>
			<p id='sport_news' class='news'>여자 배구가 올림픽 4강에 진출했습니다.</p>
			
		</div>
	</div>
	
	<div class="bottom">
		<div>copyright</div>
	</div>

</body>

</html>
'''

soup = bs(html, 'html.parser')
print(f'soup: {soup}')

#06 html hyerachy
h1 = soup.html.body.h1
print(f'h1: {h1.string}')

h2 = soup.html.body.h2
print(f'h2: {h2.string}')

#참고 next 1번은 개행문자
h2_next = soup.html.body.h2.next_sibling
print(f'h2: {h2_next.string}')

h2_next_next = soup.html.body.h2.next_sibling.next_sibling
print(f'h2: {h2_next_next.string}')

#07 find() & find_all()
news_desk = soup.find(id='news_desk')
print(f'news_desk: {news_desk.string}')

newsList = soup.find_all(class_='news')
for idx, news in enumerate(newsList):
    print(f'idx: {idx}, \t news: {news.string}')

aList = soup.find_all('a')
for idx, a in enumerate(aList):
    print(f'idx: {idx}, \t a:{a.string}')
    print(f'idx: {idx}, \t a:{a.attrs["href"]}')

#08 select_one() & select()
news_desk = soup.select_one('#news_desk')
print(f'news_desk: {news_desk.string}')

newsList = soup.select('div p.news')
for idx, news in enumerate(newsList):
    print(f'idx: {idx}, \t news: {news}')

#09 selector를 이용한 노드 선택
url = 'https://browse.gmarket.co.kr/search?keyword=%EB%82%98%EC%9D%B4%ED%82%A4%EC%9A%B4%EB%8F%99%ED%99%94'
htmlData = rq.urlopen(url)
soup = bs(htmlData, 'html.parser')
names = soup.select('#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item')
for idx, name in enumerate(names):
    # print(f'idx: {idx} \t name: {name}')
    print(f'name: {myUtil.removeSpaces(list(name)[2])}')
    # for idx1, name1 in enumerate(name):
    #     print(f'idx1: {idx1}, \t name1: {name1}')

prices = soup.select('#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong')
for idx, price in enumerate(prices):
    print(f'idx: {idx}, \t price: {myUtil.wonToInt(price.string)}')

#01 엑셀(openpyxl)에 이름, 가격 입력해보자
for i in range(len(names)):
    shoseName = myUtil.removeSpaces(list(names[i])[2])
    shosePrice = myUtil.wonToInt(prices[i].string)
    s2e.write2Excel([shoseName, shosePrice])

