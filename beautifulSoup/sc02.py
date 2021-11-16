from download import downloadData as dld

url = 'https://ssl.pstatic.net/tveta/libs/1358/1358440/f8558e92c6c55230cc93_20211012141902904.jpg'
path = 'C:/lnr_scraping/download/img/'
fileName = 'new.jpg'
# result = dld.downloadDataAtNetwork(url, path, fileName)
#
# if result == 1:
#     print('success!')
# else:
#     print('fail!')

ddan = dld.DownloadDataAtNetwork(url, path, fileName)
result = ddan.downloadData()

# if result == 1:
#     print('success')
# else:
#     print('fail')

ddan.setUrl('https://ssl.pstatic.net/tveta/libs/1353/1353461/b336bc27b90baff4202f_20211013015810698_2.jpg')
ddan.setFileName('newnewFile.jpg')
ddan.downloadData()