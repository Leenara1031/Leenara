from selenium import webdriver
from bs4 import BeautifulSoup

wd = webdriver.Chrome('./chromedriver.exe')
wd.get("https://coffeebeankorea.com/store/store.asp")

wd.execute_script("storePop2(1)")

html = wd.page_source
soupCB1 = BeautifulSoup(html, 'html.parser')
print(soupCB1.prettify())

store_name_h2 = soupCB1.select("div.store_txt > h2")
store_name_h2
store_name = store_name_h2[0].string
store_name

store_info = soupCB1.select("div.score_txt > table.store_table > tbody > tr > td")
store_info

store_adress_list = list(store_info[2])
store_adress_list
store_address = store_adress_list[0]
store_address

store_phone = store_info[3].string
store_phone