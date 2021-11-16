#Q1
#q태그의 데이터(값)을 텍스트 파일에 저장해보자!
#[2021-10-15 10:35:20] [0] 9시 뉴스입니다.
#[2021-10-15 10:35:20] [1] 오늘 뉴스입니다.
#[2021-10-15 10:35:20] [2] 간절기 감기조심하세요.

import time

#%H(1~12) %I(1~24)
lt = time.localtime()
formatedTime = time.strftime('[%Y-%m-%d %H:%M:%S]')
print(f'formatedTime : {formatedTime}')
