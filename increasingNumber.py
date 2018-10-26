def increasingNumber(x, n):
    for a in range(1,n+1):
        while x % a != 0: 
            x += 1
    return x
