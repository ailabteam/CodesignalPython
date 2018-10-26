def onlyEvenNumbers(left, right):
    t = []
    for i in range(left, right + 1):
        if i % 2 == 0:
            t.append(i)
    return t
