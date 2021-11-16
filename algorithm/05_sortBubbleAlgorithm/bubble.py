nums = [10, 2, 7, 21, 0]
print(f'not sorted nums: {nums}')

length = len(nums) - 1
for i in range(length):
    for j in range(length - i):
        if nums[j] > nums[j + 1]:
            # temp = nums[j]
            # nums[j] = nums[j+1]
            # nums[j+1] = temp
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(f'sorted nums: {nums}')

import copy

def bubbleSort(ns):
    cns = copy.copy(ns)
    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                cns[j], cns[j + 1] = cns[j + 1], cns[j]

    return cns

print(f'not sorted nums: {bubbleSort(nums)}')
print(f'not sorted nums: {nums}')

#01 새학년이되어 학급에 20명이 새로 모였다. 학생들의 키를 정렬(오름차순) 해보자!
