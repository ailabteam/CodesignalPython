def isTournament(n, fromV, toV):
    ed = []
    ed = [[False for i in range(n)] for j in range(n)]

    for i in range(len(fromV)):
        ed[fromV[i] - 1 ][ toV[i] - 1] = True

    for i in range(n):
        for j in range(i + 1, n):
            if ed[i][j] == ed[j][i]:
                return  False

    if  n * (n - 1) / 2 != len(fromV):
        return False
    return True
