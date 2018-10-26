def isPermutation(n, a):
    d = [0 for i]
    c = 0
    for i in range(len(a)):
        if a[i] <= 0:
                return False
        if a[i] > n:
                return False
        if d[a[i] - 1] == 0:
                d[a[i] - 1] = 1
                c += 1
    return c == n


