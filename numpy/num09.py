import numpy as np
import copy

#view 개념
nArr = np.arange(25).reshape(5, 5)
print(nArr)

# raw3 = nArr[2][:]
# print(raw3)
#
# raw3[2] = 99
# print(raw3)
# print(nArr)
#
# raw3[2:] = [102, 103, 104]
# print(raw3)
# print(nArr)

raw3 = copy.copy(nArr[2, :])
print(raw3)

raw3[2:] = 99
print(raw3)
print(nArr)


