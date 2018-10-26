def swapDiagonals(m):
    N = len(m)
    for i in range(N):
        m[i][i], m[i][N - i - 1] = m[i][N - i - 1], m[i][i]
    return m
