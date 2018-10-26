def weakNumbers(n):
    d = [0 for i in range(n + 1)]
    for x in range(1, n + 1):
        d[x] = 0
        y = 1
        while y * y <= x:
            if x % y == 0:
                d[x] += 2
                if y*y == x:
                  d[x] -= 1
            y += 1
    weakness = [0 for i in range(n + 1)]
    maxWeakness = 0
    cnt = 0
    for x in range(1, n + 1):
        weakness[x] = 0
        for y in range(1, x):
            if d[y] > d[x]:
                weakness[x] += 1
        if weakness[x] == maxWeakness:
            cnt += 1
        if weakness[x] > maxWeakness:
            maxWeakness = weakness[x]
            cnt = 1
    return [maxWeakness, cnt]
