def isSumOfConsecutive2(n):
    c = 0
    for i in range(1, n):
        s = i
        for j in range(i+1, n + 1):
            s += j
            if s == n:
                print i
                c += 1
    return c