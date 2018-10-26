def matrixElementsSum(m):
    res = 0
    for i in range(len(m[0])):
        for j in range(len(m)):
            if m[j][i] == 0:
                break
            res += m[j][i]
    return res
