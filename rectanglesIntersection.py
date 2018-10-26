def rectanglesIntersection(a, b, c, d):
    for i in range(2):
        if a[i] > b[i]:
            tmp = a[i]
            a[i] = b[i]
            b[i] = tmp
        if c[i] > d[i]:
            tmp = a[i]
            a[i] = b[i]
            b[i] = tmp
        if b[i] < c[i]:
            return 0
        if a[i] > d[i]:
            return 0
        
    return (max(a[0], c[0]) - min(b[0], d[0])) *(max(a[1], c[1]) - min(b[1], d[1]));
