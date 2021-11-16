import numpy as np

#버전 확인
print(f'np.__version__: {np.__version__}')

listVars = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(listVars[0][0]) #1
print(listVars[0][1]) #2
print(listVars[0][2]) #3

#배열
nums1 = [1, 2, 3]
print(f'nums1: {nums1}')
nArr = np.array(nums1)
print(f'nArr: {nArr}')
print(f'nArr: {type(nArr)}')
print(f'nArr: {len(nArr)}')
print(f'shape: {np.shape(nArr)}')
print(f'shape: {nArr.shape}')

#2차원 배열 [[, , ,], [, , ,], [, , ,]]
num1 = [1, 2, 3]
num2 = [4, 5, 6]
nArr = np.array([num1, num2])
print(f'nArr: {nArr}')
print(f'nArr.shape: {nArr.shape}')

#3x3
nArr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'nArr: {nArr}')
print(nArr.shape)

#1 5행2열 배열을 만들고, 모양(shape)을 출력해보자!
nArr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print(f'nArr: {nArr}')
print(nArr.shape)

#2 2행5열 배열을 만들고, 모양(shape)을 출력해보자!
nArr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f'nArr: {nArr}')
print(nArr.shape)

#3 for문을 이용해서 2행3열 다차원 배열을 만들고, 모양을 출력해보자!
cnt = 0
nsOutter = []
for i in range(2):
    ns1 = []
    for j in range(3):
        cnt += 1
        ns1.append(cnt)

    nsOutter.append(ns1)

nums = np.array(nsOutter)
print(f'nums: {nums}')

#4 다음과 같은 데이터를 numpy를 이용해서 다차원 배열로 만들어보자!
#이름 박찬호 박세리 이승엽 박지성 김연경
#나이  46    20    19    40    20
#종목  야구  골프  야구  축구  배구
#국적  한국  한국  한국  한국  한국
#성별   M    W    M    M    W

nd1 = ['이름', '박찬호', '박세리', '이승엽', '박지성', '김연경']
nd2 = ['나이', '46', '20', '19', '40', '20']
nd3 = ['종목', '야구', '골프', '야구', '축구', '배구']
nd4 = ['국적', '한국', '한국', '한국', '한국', '한국']
nd5 = ['성별', 'M', 'W', 'M', 'M', 'W']

temArr = np.array([nd1, nd2, nd3, nd4, nd5])
print(f'temArr: {temArr}')

#size, ndim, shape
nArr = np.array([[1, 2, 3], [4, 5, 6]])
print(f'nArr: {nArr}')
print(f'nArr type: {type(nArr)}')
print(f'nArr size: {nArr.size}')
print(f'nArr ndim: {nArr.ndim}')
print(f'nArr shape: {nArr.shape}')

#5 np를 이용해서 3차원 배열을 만들고, size, shape, ndim를 출력해보자!
nArr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f'nArr: {nArr}')
print(f'nArr size: {nArr.size}')
print(f'nArr shape: {nArr.shape}')
print(f'nArr ndim: {nArr.ndim}')
