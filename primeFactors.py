def primeFactors(n):
    r = []
    i = 2
    while n > 1:
        while n % i == 0:
            r.append(i)
            n //= i
        i += 1
    return r
