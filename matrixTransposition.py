def matrixTransposition(X):
    res = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return res
