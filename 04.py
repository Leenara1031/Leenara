import numpy as np

#덧셈 연산
nArr1 = np.array([1, 2, 3, 4, 5])
# nArr2 = np.array([3, 3, 3, 3, 3])
nArr2 = np.array([3])
nArr3 = nArr1 + nArr2
print(nArr3)

#뺄셈 연산
nArr1 = np.array([1, 2, 3, 4, 5])
# nArr2 = np.array([3, 3, 3, 3, 3])
nArr2 = np.array([3])
nArr3 = nArr1 - nArr2
print(nArr3)

#곱셈 연산
nArr1 = np.array([1, 2, 3, 4, 5])
# nArr2 = np.array([3, 3, 3, 3, 3])
nArr2 = np.array([3])
nArr3 = nArr1 * nArr2
print(nArr3)

#나눗셈 연산
nArr1 = np.array([1, 2, 3, 4, 5])
# nArr2 = np.array([3, 3, 3, 3, 3])
nArr2 = np.array([3])
nArr3 = np.round(nArr1 / nArr2, 2)
print(nArr3)
print(type(nArr3))
print(nArr3.dtype)
nArr3 = nArr3.astype(int) #nArr3 = nArr3.astype('i')
print(nArr3)

#반올림
print(round(3.1456789, 2))

#몫 연산
nArr1 = np.array([1, 2, 3, 4, 5])
nArr2 = np.array([3])
nArr3 = nArr1 // nArr2
print(nArr3)

#나머지 연산
nArr1 = np.array([1, 2, 3, 4, 5])
nArr2 = np.array([3])
nArr3 = nArr1 % nArr2
print(nArr3)

nArr1 = np.array([1, 2, 3, 4, 5]).reshape(5, 1)
nArr2 = np.array([3, 3])
nArr3 = nArr1 + nArr2
print(nArr3)

nArr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
nArr2 = np.dot(nArr1, [[3, 3, 3], [3, 3, 3], [3, 3, 3]])
print('-' * 30)
print(nArr2)




