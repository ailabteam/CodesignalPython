def maxSubarray(a):
    sum = 0
    for i in range(1,len(a)+1):
        for j in range(len(a) - i):
            s = 0
            for k in range(j, j + i):
                s += a[k]
            if s > sum:
                sum = s
    return sum