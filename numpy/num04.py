#단위 행렬
import numpy as np

nArr = np.eye(1)
print(f'{nArr}')

nArr = np.eye(2)
print(f'{nArr}')

nArr = np.eye(3)
print(f'{nArr}')

#행렬 곱셈
nArr1 = np.eye(2)
nArr2 = np.array([[10, 20], [30, 40]])

nArr3 = nArr1 * nArr2
print(f'{nArr3}')

nArr3 = np.dot(nArr1, nArr2)
print(f'{nArr3}')

#1 다음 2개의 2차원 배열에 대해서 곱셈 및 행렬곱셈 결과를 출력해보자!
print('-' * 20)
nArr1 = np.array([[2, 4, 6], [7, 3, 11], [2, 5, 4]])
nArr2 = np.array([[7, 2, 3], [8, 2, 2], [5, 8, 7]])

nArr3 = nArr1 * nArr2
print(f'{nArr3}')

print('-' * 20)
nArr3 = np.dot(nArr1, nArr2)
print(f'{nArr3}')

#2 nArr3 다차원 배열에서 처음과 마지막 요소의 합을 구하는 코드를 작성해보자!
#나의 답안
sum1 = nArr1[0] + nArr2[0]
sum2 = (nArr1 - 1) + (nArr2 - 1)

sum = 0
for i in range(sum1):
    for j in range(sum2):
        sum += nArr[i][j]

print(f'nArr: {nArr}')

#3 0을 포함한 짝수행, 0을 포함한 짝수열의 합을 구하는 코드를 작성해보자!
