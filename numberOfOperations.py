def numberOfOperations(a, b):
    n = 0
    while max(a, b) % min(a, b) == 0:
        n += 1
        a, b = max(a, b) / min(a, b), min(a, b)
    return n
