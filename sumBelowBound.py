def sumBelowBound(bound):
    n = 1
    while True :
        if n * (n + 1) > 2 * bound:
            break
        n += 1
    return n - 1
