import requests
import json

apiKey = 'ff7f997b65eb4fa3391fc281556f3df7'
cityList = ['Daejeon', 'Seoul', 'Tokyo', 'New York']
apiUrl = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

for name in cityList:
    url = apiUrl.format(city=name, key=apiKey)
    res = requests.get(url)
    dataObj = json.loads(res.text)

    print(f'{dataObj["timezone"]}')
