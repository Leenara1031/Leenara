from urllib import request as rq

#어디로부터 어떤 경로에 무슨 이름으로 저장
url = 'https://ssl.pstatic.net/tveta/libs/1338/1338324/de93c8105d30fc156ea9_20211013141149848.jpg'
path = 'C:/lnr_scraping/download/img/'
fileName = 'myBannerImg.jpg'

#request.urlretrieve(): 데이터 다운로드
try:
    rq.urlretrieve(url, path + fileName)
except Exception as e:
    print(e)
    print('image download fail!')
else:
    print('image download success!')
finally:
    print('image download process complete!')

# request.urlopen(): 데이터 로드
downloadInMemory = rq.urlopen(url).read()
print(f'downloadInMemory: {downloadInMemory}')

try:
    with open(path + fileName, 'ab') as f:
        f.write(downloadInMemory)
except Exception as e:
    print(e)
    print('image download fail!')
else:
    print('image download success!')
finally:
    print('image download process complete!')


#텍스트 파일 읽기 & 쓰기
#step01 : f = open('C:/temp/temp.txt','r')
#step02 : read() & write() str = f.read()
#step01 : close() f.close()

#example
#01 urletrieve()를 이용해서 데이터 다운로드 하는 모듈(함수, 클래스)을 만들어보자!

url = ''
path = 'C:/lnr_scraping/download/img/'
fileName = 'myBannerImg.jpg'

try:
    rq.urlretrieve(url, path + fileName)
except Exception as e:
    print(e)
    print('image download fail!')
else:
    print('image download success!')
finally:
    print('image download process complete!')

#02 urlopen()를 이용해서 데이터 다운로드 하는 모듈(함수, 클래스)을 만들어보자!

downloadInMemory = rq.urlopen(url).read()
print(f'downloadInMemory: {downloadInMemory}')

try:
    with open(path + fileName, 'ab') as f:
        f.write(downloadInMemory)
except Exception as e:
    print(e)
    print('image download fail!')
else:
    print('image download success!')
finally:
    print('image download process complete!')