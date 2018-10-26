def neighbouringElements(a):
    di = [[1,0], [0,1]]
    res = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(di)):
                if i + di[k][0] < len(a) and j + di[k][1] < len(a[0]) and a[i][j] == a[i+di[k][0]][j + di[k][1]]:
                    res += 1
    return res