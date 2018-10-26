def primeFactors(n):
    res = []
    i = 2
    while n > 1:
        while n % i == 0:
            res.append(i)
            n /= i
        i += 1
        print n
    return res
