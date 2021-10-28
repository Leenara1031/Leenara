from urllib import request as rq
from bs4 import BeautifulSoup as bs

weatherURL = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=133'
xmlData = rq.urlopen(weatherURL)
# print(f'xmlData : {xmlData}')

parseData = bs(xmlData, 'html.parser')
# print(f'parseData: {parseData}')

# titleStr = parseData.find('title').string
# print(f'titleStr: {titleStr}')

# titles = parseData.find_all('title')
# for idx, title in enumerate(titles):
#     print(f'[{idx}] [{title.string}]')

modes = parseData.find_all('mode')
tmefs = parseData.find_all('tmef')
wfs = parseData.find_all('wf')
tmns = parseData.find_all('tmn')
tmxs = parseData.find_all('tmx')
rnsts = parseData.find_all('rnst')

print(f'modes length: {len(modes)}')
print(f'tmefs length: {len(tmefs)}')
print(f'wfs length: {len(wfs)}')
print(f'tmns length: {len(tmns)}')
print(f'tmxs length: {len(tmxs)}')
print(f'rnsts length: {len(rnsts)}')

for idx, mode in enumerate(modes):
    print(f'[{idx}] [{mode.string}] [{tmefs[idx].string}] [{wfs[idx].string}] [{tmns[idx].string}] [{tmxs[idx].string}] [{rnsts[idx].string}]')
