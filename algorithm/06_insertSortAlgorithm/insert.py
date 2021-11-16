nums = [5, 10, 2, 1, 0]
print(f'not sortde nums: {nums}')

#오름차순 정렬
for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] > cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2 + 1] = cNum

print(f'nums: {nums}')

#내림차순 정렬???
for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] < cNum and i2 <= 0:
        nums[i2 + 1] = nums[i2]
        i2 += 1

    nums[i2 + 1] = cNum

print(f'nums: {nums}')