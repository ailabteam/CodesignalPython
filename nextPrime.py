def nextPrime(n):
    def f(x):
        i = 2
        while i*i <= x:
            if x % i == 0:
                return 0
            i += 1
        return x > 1

    n += 1
    while not f(n):
        n += 1
    
    return n
