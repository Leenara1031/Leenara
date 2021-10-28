import os
import sys
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "49634f5349646c7337366d51474b51"

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('urf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getSeoulStatsItem(yyyymm, national_code, ed_cd):
    service_url = "http://openapi.seoul.go.kr:8088/49634f5349646c7337366d51474b51/xml/ChunmanFreeSuggestions/1/100/"

    parameters = "?_type=json&serviceKey=" + ServiceKey
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + national_code
    parameters += "&ED_CD=" + ed_cd

    url = service_url + parameters

    retData = getRequestUrl(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def getSeoulStatsService(nat_cd, ed_cd, nStartMonth, nEndMonth):
    jsonResult = []
    result = []
    natName = ''
    dataEND = "{0}{1:0>2}".format(str(nEndMonth), str(12))
    isDataEnd = 0
    for year in range(nStartMonth, nEndMonth+1):
        for month in range(1, 13):
            if(isDataEnd == 1): break
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            jsonData = getSeoulStatsItem(yyyymm, nat_cd, ed_cd)
            if (jsonData['resonse']['header']['resultMsg'] == 'OK'):
                ifDataEnd = 1
                dataEND = "{0}{1:0>2}".format(str(year), str(month-1))
                print("데이터 없음 \n 제공되는 통계 데이터는 %s월 까지 입니다." %(str(month-1)))
                break
            print(json.dumps(jsonData, indent=4, sort_keys= True, ensure_ascii= False))

            natName = jsonData['response']['body']['items']['item']['natKorNm']
            natName = natName.replace(' ', '')
            num = jsonData['response']['body']['items']['item']['num']
            ed = jsonData['response']['body']['items']['item']['ed']
            print('[%s_%s : %s]' %(natName, yyyymm, num))
            print('-' * 30)
            jsonResult.append({'nat_name': natName, 'nat_cd': nat_cd, 'yyyymm': yyyymm, 'visit_cnt': num})
            result.append([natName, nat_cd, yyyymm, num])
    return (jsonResult, result, natName, ed, dataEND)

def main():
    jsonResult = []
    result = []
    print("<<민주주의 서울 자유 제안 정보를 수집합니다..>>")
    nStartMonth = int(input('데이터를 몇 월부터 수집할까요? : '))
    nEndMonth = int(input('데이터를 몇 월까지 수집할까요? : '))
    ed_cd = "E"
    jsonResult, result, natName, ed, dataEND = getSeoulStatsService(ed_cd, nStartMonth, nEndMonth)

    with open('./%s_%s_%d_%s.json' % (natName, ed, nStartMonth, dataEND), 'W', encoding= 'utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent= 4, sort_keys= True, ensure_ascii= False)
        outfile.write(jsonFile)

    columns = ["민주주의 서울 자유 제안"]
    result_df = pd.DataFrame(result, columns= columns)
    result_df.to_csv('./%s_%s_%d_%s.csv' % (natName, ed, nStartMonth, dataEND), index= False, encoding='cp949')

if __name__=='__main__':
    main()