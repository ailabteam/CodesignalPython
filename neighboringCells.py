def neighboringCells(m):
    n = [] 
    for i in range(len(m)):
        n += [[]]
        for j in range(len(m[0])):
            t = 4
            if i-1 < 0: t-=1 
            if j-1 < 0: t-=1  
            if i+1 >= len(m): t-=1 
            if j+1 >= len(m[0]): t-=1             
            
            n[-1] += [t]
    return n 
