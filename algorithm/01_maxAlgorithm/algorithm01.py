#최댓값 알고리즘
nums = [-2, -4, 5, 7, 10, 0, 8, 20, -11]
# maxNum = max(nums)
# print(f'maxNum: {maxNum}')

#알고리즘
# def getMaxNum(ns):
#     ns.sort()
#     return ns[len(ns) -1]
#
# maxNum = getMaxNum(nums)
# print(f'maxNum: {maxNum}')

#알고리즘
# def getMaxNum(ns):
#     maxNum = -1000
#     for n in nums:
#         if maxNum < n:
#             maxNum = n
#
#     return maxNum
#
# maxNum = getMaxNum(nums)
# print(f'maxNum: {maxNum}')

#리스트에서 아스키코드가 가장 큰 값을 찾는 알고리즘을 만들어보자!
chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']

import maxModule
ma = maxModule.MaxAlgorithm(chars)
maxChar = ma.getMaxChar()
print(f'maxChar: {maxChar}')

#리스트에서 아스키코드가 가장 작은 값을 찾는 알고리즘을 만들어보자!
chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']

import minModule
ma = minModule.MinAlgorithm(chars)
minChar = ma.getMinChar()
print(f'minChar: {minChar}')

print(ord('x'))
print(ord('A'))




