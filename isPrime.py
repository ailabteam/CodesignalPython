def isPrime(n):
    if n < 2: 
        return False
    if n == 2 or n == 3:
        return True
    j = int(math.sqrt(n))
    for i in range(2, j+1):
        if n % i == 0:
            return False
    return True
