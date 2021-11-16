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

h1 = soup.html.body.h1
h2 = soup.html.body.h2
h2_next = soup.html.body.h2.next_sibling
h2_next_next = soup.html.body.h2.next_sibling.next_sibling

print(f'h1: {h1.string}')
print(f'h2: {h2.string}')
print(f'h2_next: {h2_next.string}')
print(f'h2_next_next: {h2_next_next.string}')
print(f'=====')