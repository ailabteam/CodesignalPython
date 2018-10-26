def isIdentityMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i==j:
                if m[i][j]!=1:
                    return 0
            else:
                if m[i][j]:
                    return 0
    return 1

