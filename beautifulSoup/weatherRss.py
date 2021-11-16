#Q1
#사용자가 지역(행정)코드를 입력하면 해당 지역의 날씨 정보(RSS)가 출력되는 모듈을 만들어보자!

#Q2
#Q1을 해결한 후 유효한 행정 코드가 아닌 경우 '유효한 행정코드가 아닙니다. 다시 입력하세요.'

from urllib import request as rq
from urllib import request as ps

def weatherRSSReader(url):

    url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

    while True:
        locationCode = input('please input location code : ')
        result = availableLocationCode(locationCode)
        if result == 1:
            print('available code')

            locationCodeDic = {'stnId': locationCode}
            params = ps.urlencode(locationCodeDic)

            url = url + '?' + 'stnId' + locationCode
            rssData = rq.urlopen(url).read()
            rssText = rssData.decode('UTF-8')
            print(f'rssText: {rssText}')

            break

        else:
            print('not available code')


def availableLocationCode(code):

    codes = {
        '108' : '전국',
        '109' : '서울, 경기',
        '105' : '강원도',
        '131' : '충북',
        '133' : '충남',
        '146' : '전북',
        '156' : '전남',
        '143' : '경북',
        '159' : '경남',
        '184' : '제주도'
    }

    # print(f'codes: {codes}')

    result = 0
    if code in codes:
        print('available code')
        result = 1
    else:
        print('not available code')
        result = 0

    return result

class WeatherRSSReader:

    def __init__(self, lc = '108'):
        self.url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
        self.locationCode = lc

    def printWeatherRSS(self):

        while True:
            inputCode = input('please location code:')
            result = availableLocationCode(inputCode)
            if result == 1:
                print('available code')
                self.setLocationCode(inputCode)
                locationDic = {'stnId': self.locationCode}
                params = ps.urlcode(locationDic)
                rssURL = self.url + '?' + params

                rssData = rq.urlopen(rssURL).read()
                rssText = rssData.decode('UTF-8')
                print(rssText)

                break

        else:
            print('not available code')

    def setLocationCode(self, lc):
        self.locationCode = lc
    def getLocationCode(self):
        return self.locationCode

if __name__== '__mail__':
    availableLocationCode(108)