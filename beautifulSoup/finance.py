from urllib import request as rq
from bs4 import BeautifulSoup as bs
import time
import mariadb

for i in range(20):

    financeNewsURL = f'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259={i}'

    financeNewsHTML = rq.urlopen(financeNewsURL)
    financeNewsText = bs(financeNewsHTML, 'html.parser')

    main_content = financeNewsText.find('div', {'id':'main_content'})

    dls = main_content.find_all('dl')

    for idx, dl in enumerate(dls):
        dts = dl.find_all('dt')

        #title #title_href
        title = ''
        title_href = ''
        imgUrl = ''

        if len(dts) == 1:
            title_href = dts[0].find('a').attrs['href']
            title = dts[0].find('a').string.strip()
        elif len(dts) == 2:
            imgUrl = dts[0].find('a').find('img').attrs['src']
            title_href = dts[0].find('a').attrs['href']
            title = dts[1].find('a').string.strip()

            imgFileName = str(time.time()).replace('.', '') + '.jpg'
            rq.urlretrieve(imgUrl,
                           './C:/lnr_scraping/naverNews/newsViewerPjt/src/main/webapp/resources/newImgs/' + imgFileName)

        #article
        lede = dl.find('span', {'class':'lede'}).string

        #publisher
        writing = dl.find('span', {'class': 'writing'}).string

        print(f'title[{idx}]: {title}')
        print(f'title_href[{idx}]: {title_href}')
        print(f'imgUrl[{idx}]: {imgUrl}')
        print(f'lede[{idx}]: {lede}')
        print(f'writing[{idx}]: {writing}')

        conn = mariadb.connect(host='localhost', port=3306, user='root', password='0000', db='newsdb')
        cur = conn.cursor()

        n_title = title; n_title_href = title_href; n_photo_name = imgFileName
        n_article = lede; n_publisher = writing

        if n_article == None:
            n_article = 'null'

        sql = 'INSERT INTO tbl_news(n_title, n_title_href, n_photo_name, n_article, n_publisher, n_reg_date) ' \
              'VALUES(?, ?, ?, ?, ?, NOW())'

        cur.execute(sql, (n_title.encode('utf-8'), n_title_href, n_photo_name, n_article, n_publisher))

        conn.commit()
        conn.close()
