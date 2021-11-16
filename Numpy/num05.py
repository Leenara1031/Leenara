import numpy as np

# for i in range(1, 10, 5):
#     print(i)

# nArr1 = np.arange(0, 10, 1) #0, 1, 2 ... 10
# nArr2 = np.arange(10, -1, -1) #10, 9, 8 ...0
# print(nArr1, nArr2)

nArr1 = np.arange(0, 12, 1)

#3 X 4
r_nArr1 = nArr1.reshape(3, 4)
print(r_nArr1)

#1 x 12
r_nArr1 = nArr1.reshape(1, 12)
print(r_nArr1)

#1 nArr1에서 reshape 할 수 있는 모든 경우를 출력해보자!
#2 주식정보를 가져와서 다차원 배열로 저장해보자!