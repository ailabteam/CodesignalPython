def isPower(n):
    j = int(math.sqrt(n))
    for i in range(1, j+1):
        t = i
        for k in range(1, 400):
            t *= k
            if t == n:
                return True
    return False
