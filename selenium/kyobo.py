from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')
bsObject = BeautifulSoup(html, "html.parser")

bookPageUrls = []
for cover in bsObject.find_all('div', {'class': 'detail'}):
    link = cover.select('a')[0].get('href')
    bookPageUrls.append(link)

for index, bookPageUrls in enumerate(bookPageUrls):
    html = urlopen(bookPageUrls)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('meta', {'property': 'og:title'}).get('content')
    author = bsObject.select('span.name a')[0].text
    price = bsObject.find('meta', {'property': 'og:price'}).get('content')
    image = bsObject.find('meta', {'property': 'og:image'}).get('content')
    url = bsObject.find('meta', {'property': 'og:url'}).get('content')

    print(f'bestseller, {index + 1}위')
    print(f'title, {title}')
    print(f'author, {author}')
    print(f'{price}원')
    print(f'{image}, {url}')

result = []

book_tbl = bookPageUrls.DataFrame(result, columns = ('title', 'author', 'price', 'image', 'url'))
bookPageUrls.xlsx('./bookPageUrls.xlsx', encoding= 'cp949', mode= 'w', index= True)