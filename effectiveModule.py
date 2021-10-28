#sc21

def getEffectibeTrs():

    trs = []

    n = 3
    while True:
        for i in range(5):
            trs.append(n)
            n += 1

    for i in range(3):
        n += 1

        if len(trs) >= 30: break

    return trs