#앞뒤 공백 제거
def removeSpaces(str):
    return str.strip()

#원 단위 콤마 제거 to Integer
#[0:5], join
def wonToInt(won):
    price = won.split(',')
    return int(''.join(price[:]))

#숫자를 원단위 표기로 변경
def intToWon(won):
    return format(won, ',')

#text 전역변수
if __name__=='__main__':
    print(removeSpaces('   나이키 코르테즈    '))
    print(wonToInt('234,567,890,000'))
    print(type(wonToInt('234,567,890,000')))
    print(intToWon(234567890000))
    print(type(intToWon(234567890000)))