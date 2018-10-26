def smallestUnusualNumber(a):
    prd = 1
    sm = 0
    for v in a:
        d = ord(v) - ord('0')
        prd *= d
        sm += d 
        if v == '0':
            return 0
    if sm > prd:
        return 0
    return 10-(ord(a[-1])-ord('0'))
