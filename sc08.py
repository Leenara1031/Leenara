from bs4 import BeautifulSoup
import time

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
pTags = soup.find_all('p')
print(f'pTags: {pTags}')

def getFomatedTime():

    lt = time.localtime()
    formatedTime = time.strftime('[%Y-%m-%d %H:%M:%S]')

    return formatedTime

    # print(f'formatedTime : {formatedTime}')

def getIdxToStringType(idx):
    return '[' + str(idx) + ']'

for idx, element in enumerate(pTags):

    currentTime = getFomatedTime()
    # print(f'{currentTime} [{idx}] {element.string}')

    with open('C:/lnr_scraping/download/p_log.txt', 'a') as f:
        f.write(currentTime + getIdxToStringType(idx) + element.string + '\n')

    # print(f'idx: {idx}, \t element: {element.string}')

#Q1
#q태그의 데이터(값)을 텍스트 파일에 저장해보자!
#[2021-10-15 10:35:20] [0] 9시 뉴스입니다.
#[2021-10-15 10:35:20] [1] 오늘 뉴스입니다.
#[2021-10-15 10:35:20] [2] 간절기 감기조심하세요.

#Q2
#네이버 메인페이지에서 <a>태그에 해당하는 데이터를 몽땅 가져와서 텍스트 파일에 저장해보자!


