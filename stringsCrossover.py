def stringsCrossover(a, r):
    c = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ok = 1
            for k in range(len(r)):
                if not r[k] in [a[i][k], a[j][k]]:
                    ok = 0
                    break
            if ok:
                c += 1
    return c
