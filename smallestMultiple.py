def smallestMultiple(left, right):
    res = 1
    cur = right +1
    
    if left == 1 and right == 1:
        return 1
    
    while True:
        if all([cur % x == 0 for x in range(left, right+1)]):
            return cur
        cur += 1
        
    return 0
