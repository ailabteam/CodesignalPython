def sumOfMultiples(n, k):
    t = 0
    for i in range(n+1):
        if i % k  == 0:
            t += i
    return t
