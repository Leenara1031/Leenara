#선형 검색(보초법)
datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

inputNum = int(input('input integer: '))
searchResultIdx = -1

datas.append(inputNum)
print(f'datas: {datas}')

n = 0
while True:

    if datas[n] == inputNum:
        if n != len(datas) -1:
            searchResultIdx = n
        break

    n += 1

print(f'searchResultIdx: {searchResultIdx}')

#[4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
#01 리스트에서 가장 앞에 있는 '7'을 검색하고 위치(인덱스)를 출력하자!
#02 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력하자!

