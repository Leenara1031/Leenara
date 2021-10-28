import copy

def insertSort(ns, isAsc=True, deepCopy=True):

    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns = ns

    for i1 in range(1, len(ns)):
        i2 = i1 - 1
        cNum = cns[i1]

        if isAsc:
            while cns[i2] > cNum and i2 >= 0:
             cns[i2 + 1] = cns[i2]
             i2 -= 1
        else:
            while cns[i2] < cNum and i2 >= 0:
                cns[i2 + 1] = cns[i2]
                i2 -= 1

        ns[i2 + 1] = cNum

    return cns

