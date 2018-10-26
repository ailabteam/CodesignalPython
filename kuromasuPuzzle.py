def kuromasuPuzzle(b):
    m = len(b)
    n = len(b[0])
    r = [[0 for i in range(n)] for j in range(m)]
    print m
    print n
    print r
            
    for i in range(m):
        for j in range(n):
            if b[i][j] == '#':
                cnt = 0
                ii = i - 1 
                while ii >= 0 and b[ii][j] != '*':
                    cnt += 1
                    ii -= 1
                
                ii = i + 1
                while ii < m and b[ii][j] != '*':
                    cnt += 1
                    ii += 1
                
                jj = j - 1
                while jj >= 0 and b[i][jj] != '*': 
                    cnt += 1
                    jj -= 1
                
                
                jj = j + 1
                while jj < n and b[i][jj] != '*':
                    cnt += 1
                    jj += 1
                    
                r[i][j] = cnt + 1
            else:
                r[i][j] -= 1
    return r
            
    
