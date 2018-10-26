def nextSecond(t):
    t[2] += 1
    if t[2] == 60:
        t[2] = 0
        t[1] += 1
    if t[1] == 60:
        t[1] = 0
        t[0] += 1
    if t[0] == 24:
        t[0] = 0
    return t