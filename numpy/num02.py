#다차원 배열
import random

import numpy as np

nArr= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f'nArr: {nArr}')
print(f'nArr shape: {nArr.shape}')

#1 reshape
r_nArr = nArr.reshape(5, 2)
print(f'r_nArr: {r_nArr}')
print(f'r_nArr shape: {r_nArr.shape}')
print(f'r_nArr shape: {np.shape(r_nArr)}')

#2 zeros
nArr = np.zeros((2, 5))
print(f'nArr: {nArr}')
print(f'nArr shape: {nArr.shape}')
print(type(nArr[0][0]))

#3 ones
nArr = np.ones((5, 2))
print(f'nArr: {nArr}')
print(f'nArr shape: {nArr.shape}')

#4 data search
nArr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(f'nArr[0][0]: {nArr[0][0]}')
print(f'nArr[0][0]: {nArr[0][1]}')
print(f'nArr[0][0]: {nArr[0][2]}')
print(f'nArr[0][0]: {nArr[0][3]}')
print(f'nArr[0][0]: {nArr[0][4]}')

print(f'nArr[1][0]: {nArr[1][0]}')
print(f'nArr[1][1]: {nArr[1][1]}')
print(f'nArr[1][2]: {nArr[1][2]}')
print(f'nArr[1][3]: {nArr[1][3]}')
print(f'nArr[1][4]: {nArr[1][4]}')

#1 반복문을 이용해서 다차원 배열의 모든 데이터를 조회하자!
nArr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
sha = nArr.shape
print(f'sha: {sha}')

for i in range(sha[0]):
    for j in range(sha[1]):
        print(nArr[i][j])

#2 shape가 (2, 3, 4)인 다차원 배열을 만들자!
#random module 데이터 생성!
import random

sha = 2, 3, 4,
nArr = np.zeros(sha)
print(f'nArr: {nArr}')

for i in range(sha[0]):
    for j in range(sha[1]):
        for k in range(sha[2]):
            nArr[i][j][k] = random.randint(0, 10)

print(f'nArr: {nArr}')