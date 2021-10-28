import numpy as np

nArr = np.arange(36).reshape(6, 6)
print(nArr)

print(nArr[1][2])
print(nArr[4][1])

print(nArr[1, 2])
print(nArr[4, 1])

print(nArr[3, [1, 3, 5]])

#파이썬 슬라이싱
# numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
# print(numbers[1:6])
# print(numbers[1:])
# print(numbers[:6])
# print(numbers[1:6])
# print(numbers[1:6:2])
# print(numbers[1::2])
# print(numbers[::2])
# print(numbers[2:-2:2])
# print(numbers[-9:-2:2])

#numpy 슬라이싱
nArr = np.arange(36).reshape(6, 6)
print(nArr[1, ])
print(nArr[1,:])
print(nArr[:,:])
print(nArr[1:4,])
print(nArr[1:4:2,])

#column 조회
print(nArr[:,1])
print(nArr[:,1:4])
print(nArr[:,:2])

#row & column 조회
print(nArr[2:5,1:4])
print(nArr[2:5,0:5:2])
print(nArr[::2,::3])
print(nArr[0, :-2])
print(nArr[-1, -1])