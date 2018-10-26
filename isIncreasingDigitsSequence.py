def isIncreasingDigitsSequence(n):
    digit = n % 10
    n /= 10
    while n > 0:
        if n % 10 >= digit:
            return False
        digit = n % 10
        n /= 10
    return True