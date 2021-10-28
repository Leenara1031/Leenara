import random

nums = random.sample(range(0, 50), 20)
print(f'nums: {nums}')

inputNumber = int(input('input number: '))
print(f'inputNumber: {inputNumber}')

nearNum = 0
nearIdx = 0
minNum = 50

for i, n in enumerate(nums):
    absNum = abs(n - inputNumber)
    if absNum < minNum:
        minNum = absNum
        nearNum = n
        nearIdx = i

print(f'nearIdx : {nearIdx}, \t nearNum: {nearNum}')