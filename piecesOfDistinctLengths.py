def piecesOfDistinctLengths(n):
    c = 0
    for i in range(1, min(n,100002)):
        t = i * (i + 1)/2
        c += 1
        if t == n:
            return c
        elif t > n:
            break
        
    print c
    return c - 1
