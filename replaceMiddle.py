def replaceMiddle(a):
    l = len(a) / 2
    if len(a) % 2 == 0:
        return a[:l-1] + [a[l-1] + a[l]] + a[l+1:]
    return a
