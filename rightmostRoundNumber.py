def rightmostRoundNumber(a):
    idx = -1
    for i in range(len(a)):
        if a[i] % 10 == 0:
            idx = i
    return idx
