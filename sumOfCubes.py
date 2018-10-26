def sumOfCubes(n):
    t = 0
    for i in range(1,n+1):
        t += i * i * i
    return t
