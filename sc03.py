from urllib import request as rq
from urllib import parse as ps

# XML 데이터 로드
# rssURL = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=133'
# rssURLData = rq.urlopen(rssURL).read()
# rssText = rssURLData.decode('UTF-8')
# # print(f'rssURLData : {rssURLData}')
# print(f'rssText : {rssText}')

# XML 데이터 로드(parse 이용)
rssURL = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
locationCode = {'stdId' : '133'}
params = ps.urlencode(locationCode)
print(f'params : {params}')

rssURL = rssURL + '?' + params
print(f'rssURL : {rssURL}')

rssData = rq.urlopen(rssURL).read()
rssText = rssData.decode('UTF-8')
print(f'rssText : {rssText}')