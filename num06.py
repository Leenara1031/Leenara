#01 재귀함수를 이용해서 다차원 배열의 합을 구해보자!
import numpy as np

def selfSum(arr):
    sha = arr.shape
    dim = arr.ndim
    sum = 0

    if dim > 1:
        for i in range(sha[0]):
            sum += selfSum(arr[i])
        return sum

    else:
        for i in range(sha[0]):
            sum += arr[i]
        return sum


#02 다차원 배열에서 처음과 마지막 요소의 합을 구하는 코드를 작성해보자!
#03 (0을 포함한 짝수행, 0을 포함한 짝수열)의 합을 구하는 코드를 작성해보자!

#04 nArr1에서 reshape 할 수 있는 모든 경우를 출력해보자!
nArr1 = np.arange(0, 12, 1)

arr = np.array([[76, 68, 56], [128, 108, 104], [74, 46, 44]])
print(f'Arr : {arr}')

list = []
for i in range(arr.size):
    if arr.size % (i + 1) == 0:
        list.append([(i + 1), arr.size//(i + 1)]) #(1,12) (2,6) (3,4) (4,3) (6,2) (12,1)

for i in range(len(list)):
    rArr = arr.reshape(list[i][0], list[i][1])
    print(f'{i}번째 행렬: {rArr}')

#05 주식정보를 가져와서 다차원 배열로 저장해보자!