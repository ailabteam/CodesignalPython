def isSumOfConsecutive(n):
    for i in range(1, n):
        num = n
        c = i
        while num > 0:
            num -= c
            c += 1
        if num == 0:
            return True
    return False
