def numbersGrouping(a):
    v = 1000001*[0]
    for x in a:
        v[(x - 1) / 10000 + 1] += 1
        
    r = 0
    for x in v:
        if x > 0:
            r += x + 1
    
    return r
