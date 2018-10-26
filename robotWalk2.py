def robotWalk(a):
    for i in range(1, len(a) - 2):
        if a[i] <= a[i+2]:
            return True
    return False
