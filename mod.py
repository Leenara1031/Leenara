class MaxAlgorithm:

  def __init__(self, ns):
    self.nums = ns
    self.maxNum = 0
    self.maxNumIdx = 0

  def setMaxNumAndIdx(self):
    self.maxNum = self.nums[0]
    self.maxNumIdx = 0

    for i, n in enumerate(self.nums):
      if self.maxNum < n:
          self.maxNum = n
          self.maxNumIdx = i

  def getMaxNum(self):
    return self.maxNum

  def getMaxIdx(self):
    return self.maxNumIdx

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
maxAlo = MaxAlgorithm(nums)
maxAlo.setMaxNumAndIdx()
maxNum = maxAlo.getMaxNum()
maxIdx = maxAlo.getMaxIdx()
print(f'maxNum: {maxNum}')

indexes = [0 for i in range(maxNum + 1)]
print(f'indexes : {indexes}')
print(f'indexes length: {len(indexes)}')

for n in nums:
  indexes[n] = indexes[n] + 1
print(f'indexes: {indexes}')

maxAlo = MaxAlgorithm(indexes)
maxAlo.setMaxNumAndIdx()
maxNum = maxAlo.getMaxNum()
maxIdx = maxAlo.getMaxIdx()
print(f'maxNum: {maxNum}')
print(f'maxIdx: {maxIdx}')

print(f'따라서, {maxIdx}의 빈도수가 {maxNum}로 가장 높아요!')

while sum(indexes) != 0:
  maxAlo = MaxAlgorithm(indexes)
  maxAlo.setMaxNumAndIdx()
  maxNum = maxAlo.getMaxNum()
  maxIdx = maxAlo.getMaxIdx()

  print(f'{maxIdx}의 빈도수 \t{maxNum}')
  indexes[maxIdx] = 0

price = '123,450'
newPrice = price.replace(',', '')
print(newPrice)