def inversePermutation(p):
    r = len(p) * [0]
    for i in range(len(p)):
        r[p[i]-1] = i + 1
    return r
