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
			<p>9시 뉴스입니다.</p>

			<h2>오늘 주요 뉴스</h2>
			<p>오늘 뉴스입니다. 드디어 코로나 19가 종식 되었습니다. 마스크 벗으세요.</p>

			<h2>오늘 날씨</h2>
			<p>간절기 감기조심하세요.</p>

		</div>
	</div>

	<div class="bottom">
		<div>copyright</div>
	</div>

</body>

</html>
'''

soup = BeautifulSoup(html, 'html.parser')
news_desk = soup.select_one('p#news_desk')
print(f'news_desk: {news_desk.string}')

h1 = soup.select_one('h1')
print(f'h1: {h1}')

h2s = soup.select('h2')
print(f'h2s: {h2s}')
print(f'Type of h2s: {type(h2s)}')

# div.nav .menu_wrap a[href]
_as = soup.select('div.nav .menu_wrap a')

for a in _as:
    print('f{a.attrs["href"]}')