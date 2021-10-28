#openweathermap.org
#openweathermap API(Application Programming Interface)
#openweathermap API key
#requests 모듈(data load)
#json 모듈

import requests
import json

apiKey = 'ff7f997b65eb4fa3391fc281556f3df7'
cityList = ['Seoul', 'Tokyo', 'New York', 'Harbin']
api = 'http://api.openweathermap.org/data/2.5/seather?q={city}&appid={key}&lang=kr'

for name in cityList:
    url = api.format(city=name, key=apiKey)
    res = requests.get(url)
    data = json.loads(res.text)

    print(f'base: {data["base"]}')
    print(f'visibility: {data["visibility"]}')
    print(f'dt: {data["dt"]}')
    print(f'timezone: {data["timezone"]}')
    print(f'id: {data["id"]}')
    print(f'name: {data["name"]}')
    print(f'cod: {data["cod"]}')
    print(f'coord lon: {data["codrd"]["lon"]}')
    print(f'coord lat: {data["codrd"]["lat"]}')
    print(f'coord lat: {data["coord"]["weather"][0]["id"]}')
    print('-' * 50)
    print()

#01 주요 10개국의 날씨 정보를 엑셀 파일에 저장하자!
#02 위의 데이터를 mariaDB에 저장하자! -> spring f/w 서버프로그램 구현