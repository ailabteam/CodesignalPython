def maxSubmatrixSum(matrix, n, m):
    mx = -100000
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - m + 1):
            res = 0
            for k in range(i, i + n):
                for r in range(j, j + m):
                    if k < len(matrix) and r < len(matrix[0]):
                        res += matrix[k][r]
            print res
            mx = max(res, mx)
    return mx
            
