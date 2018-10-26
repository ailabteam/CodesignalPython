def primeFactors2(n):
    t = []
    i = 2
    while n > 1:
        ok = True
        while(n % i == 0):
            n /= i
            ok = False
        if not ok:
            t.append(i)
        i += 1
    return t
