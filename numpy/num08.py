import numpy as np

#7행 8열 배열 생성
nArr = np.arange(56).reshape(7, 8)
print(nArr)

#2행 4열 데이터 출력
print('-' * 30)
print(nArr[1,3])

#첫행 5열 데이터 출력
print('-' * 30)
print(nArr[0,4])

#마지막행 3열 데이터 출력
print('-' * 30)
print(nArr[-1,2])

#3행의 2~5열 데이터 출력
print('-' * 30)
print(nArr[2, 1:5])

#6행의 1,3,4열 데이터 출력
print('-' * 30)
print(nArr[5, [0,2,3]])

#5행의 첫번째열 데이터 출력
print('-' * 30)
print(nArr[4, 0])

#2행의 마지막열 데이터 출력
print('-' * 30)
print(nArr[1, -1])

#2행의 모든 데이터 출력
print('-' * 30)
print(nArr[1, ])

#5열의 모든 데이터 출력
print('-' * 30)
print(nArr[:, :4])

#4열 미만열의 모든 데이터 출력
print('-' * 30)
print(nArr[:, :3])

#2열 초과 5열 미만의 모든 데이터 출력
print('-' * 30)
print(nArr[:, 2:4])

#홀수행의 모든 데이터 출력
print('-' * 30)
print(nArr[::2, :])

#짝수행의 모든 데이터 출력
print('-' * 30)
print(nArr[1::2, :])

#홀수열의 모든 데이터 출력
print('-' * 30)
print(nArr[:, ::2])

#짝수열의 모든 데이터 출력
print('-' * 30)
print(nArr[:, 1::2])

#6행에서 3부터 6열까지 출력
print('-' * 30)
print(nArr[5, 2:6])

#6행에서 3부터 마지막열까지 출력
print('-' * 30)
print(nArr[5, 2:])

#3행에서 처음부터 마지막 열까지 2단계로 출력
print('-' * 30)
print(nArr[2, ::2])

#2행에서 처음부터 마지막에서 두번째까지 2단계로 출력
print('-' * 30)
print(nArr[1, :-1:2])

#첫행에서 마지막행까지 3단계 항에서 처음부터 마지막에서 두번째까지 2단계로 출력
print('-' * 30)
print(nArr[::3, ::2])