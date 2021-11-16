from bs4 import BeautifulSoup

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
			<p id="news_desk" class="news">9시 뉴스입니다.</p>

			<h2>오늘 주요 뉴스</h2>
			<p id="today_news" class="news">오늘 뉴스입니다. 드디어 코로나 19가 종식 되었습니다. 마스크 벗으세요.</p>

			<h2>오늘 날씨</h2>
			<p id="today_weather" class="news">간절기 감기조심하세요.</p>

		</div>
	</div>

	<div class="bottom">
		<div>copyright</div>
	</div>

</body>

</html>
'''

soup = BeautifulSoup(html, 'html.parser')

pTag1 = soup.find(id='news_desk')
pTag2 = soup.find(id='today_news')
pTag3 = soup.find(id='today_weather')

print(f'pTag1: {pTag1.string}')
print(f'pTag2: {pTag2.string}')
print(f'pTag3: {pTag3.string}')

pTags = soup.find_all(class_='news')
print(f'pTags:{pTags}')
print(f'Type of pTags:{type(pTags)}')
# print(f'Type of pTags:{type(list(pTags))}')

for idx, p in enumerate(pTags):
    print(f'index:{idx}, \t p:{p.string}')

pTags5 = soup.find_all('p', class_='news')
pTags5 = soup.find_all('div', class_='news')

for idx, p in enumerate(pTags5):
    print(f'index:{idx}, \t p:{p.string}')