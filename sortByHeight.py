def sortByHeight(a):
    arr = []
    for i,e in enumerate(a):
        if e == -1:
            arr.append(i)
    print arr
    a = sorted(a)
    print a
    a = a[len(arr):]
    print a
    for e in arr:
        a.insert(e, -1)
    return a
