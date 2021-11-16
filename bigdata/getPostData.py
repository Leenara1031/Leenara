import datetime

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pData = datetime.datetime.strptime(post['pubData'], '%Y-%m-%d %H:%M:%S +0900')
    pData = pData.strptime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'org_link':org_link, 'link':org_link, 'pDate':pData})
    return