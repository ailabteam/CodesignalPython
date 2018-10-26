def setDifference(a, b):

    a.sort()
    b.sort()
    C = []

    pos_b = 0
    for pos_a in range(len(a)):
        while  pos_b < len(b) - 1 and a[pos_a] > b[pos_b] :
            pos_b += 1
        if a[pos_a] != b[pos_b]:
            C.append(a[pos_a])

    return C
