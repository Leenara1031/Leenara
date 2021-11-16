import numpy as np

nArr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

#1 다차원 배열의 모든 아이템(요소)의 합을 구하자!
sha = nArr.shape
print(f'sha: {sha}')

sum = 0
for i in range(sha[0]):
    for j in range(sha[1]):
        sum += nArr[i][j]

print(f'sun: {sum}')

#재귀함수를 이용해서 다차원 배열의 합을 구해보자!
