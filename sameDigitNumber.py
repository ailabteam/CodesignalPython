def sameDigitNumber(n):
    c = n % 10
    n /= 10
    while n > 0:
        if c != n % 10:
            return False
        n /= 10
    return True
        
