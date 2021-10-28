from urllib import request as rq
from urllib import parse as ps
from bs4 import BeautifulSoup as bs

rssURL = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

locationCode = {'stdId':'133'}
params = ps.urlencode(locationCode)

rssURL = rssURL + '?' + params
print(f'rssURL: {rssURL}')

rssData = rq.urlopen(rssURL)

bsObj = bs(rssData, 'html.parser')

title = bsObj.select_one('title')
print(f'title: {title.string}')

titles = bsObj.select('title')
print(f'titles length: {len(titles)}')

for title in titles:
    print(f'title: {title.string}')

tm = bsObj.select_one('description > header > tm')
print(f'tm: {tm.string}')

wf = bsObj.select_one('description > header > wf')
print(f'tm: {wf.string}')

modes = bsObj.select('data > mode')
tmEfs = bsObj.select('data > tmEf')
wfs = bsObj.select('data > wf')
tmns = bsObj.select('data > tmn')
tmxs = bsObj.select('data > tmx')
rnSts = bsObj.select('data > rnSt')

for i in range(len(modes)):
    print('-' * 50)
    print(f'mode: {modes[i].String}')
    print(f'tmEf: {tmEfs[i].String}')
    print(f'wf: {wfs[i].String}')
    print(f'tmn: {tmns[i].String}')
    print(f'tmx: {tmxs[i].String}')
    print(f'rnSt: {rnSts[i].String}')
    print('-' * 50)


