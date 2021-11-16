datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력'))
searchIndex = -1

staIdx = 0
endIdx = len(datas) - 1
midIdx = (staIdx + endIdx) // 2
midVal = datas[midIdx]
print(f'midIdx: {midIdx}')
print(f'midVal: {midVal}')

while searchData <= datas[len(datas) -1] and searchData >= datas[0]:

    if searchData == datas[len(datas) -1]:
        searchIndex = len(datas) -1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData == midVal:
        searchIndex = midIdx
        break

print(f'searchIndex: {searchIndex}')

#[4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
#01 리스트를 오름차순으로 정렬한 후 '7'을 검색하고 위치(인덱스)를 찾아보자!