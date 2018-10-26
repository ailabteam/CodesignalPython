def makeArrayConsecutive(a):
    mn = min(a)
    mx = max(a)
    res = []
    for i in range(mn, mx):
        ok = True
        print i
        for j in range(0, len(a)):
            if i == a[j]:
                ok = False
                break
        if ok:
            res.append(i)
    return res
        
