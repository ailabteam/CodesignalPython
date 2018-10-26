def powersOfTwo(n):
    res = []
    while n > 0:
        print n
        res.append(n % 2)
        n /= 2
    kq = []
    for i in range(len(res)):
        if(int(res[i]) != 0):
            kq.append(int(res[i]) * 2**i)
    return kq
