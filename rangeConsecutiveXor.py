def f(x):
    v = [x, 2, x+2, 0]
    return v[x/2 % 4]

def rangeConsecutiveXor(l, r):
    return f(r) ^ f(l-1)
