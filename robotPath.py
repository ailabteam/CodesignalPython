def robotPath(a, bound):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    h = 'LURD'
    x = 0
    y = 0
    
    for i in range(len(dx)):
        print(i)
        print(h[i])
    
    for i in range(len(a)):
        idx = 0
        for j in range(len(h)):
            if a[i] == h[j]:
                idx = j
        if (abs(x + dx[idx]) <= bound
        and abs(y + dy[idx]) <= bound):
            x += dx[idx]
            y += dy[idx]

    return [x, y]
