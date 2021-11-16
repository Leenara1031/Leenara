#선형 검색
import lineSearchModule01 as lsm

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

inputNum = int(input('input integer: '))
searchResultIdx = -1

lsmObj = lsm.SearchData(datas, inputNum)
result = lsmObj.getIndexOfData()

if result < 0:
    print('nothing')
else:
    print(f'index of data: {result}')

# n = 0
# while True:
#
#     if n == len(datas):
#         searchResultIdx = -1
#         break
#
#     elif datas[n] == inputNum:
#         searchResultIdx = n
#         break
#
#     n += 1
#
# if searchResultIdx < 0:
#     print('nothing')
# else:
#     print(f'searchResultIdx: {searchResultIdx}')

# for idx, i in enumerate(datas):
#
#     if inputNum == i:
#         print(f'idx : {idx}')
#
#         if idx == len(datas) -1:
#             print('nothing')
