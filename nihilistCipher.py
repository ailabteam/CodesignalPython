def nihilistCipher(s, k, r, c):
    po = 26*[0]
    x = 1
    y = 1
    for l in k:
        l_ = ord(l) - ord('a')
        po[l_] = x*10 + y
        y += 1
        if y == 6:
            x += 1
            y = 1
        
    for l in range(26):
        if po[l] == 0:
            po[l] = x*10+y
            y += 1
            if y == 6:
                x += 1
                y = 1
    
    for i in range(len(po)):
        if po[i] == 61:
            po[i] = r*10 + c
            
    i = 0
    while len(k) < len(s):
        k += k[i]
        i += 1
        
    while len(k) > len(s):
        s += s[i]
        i += 1
    
    return [po[ord(s[i]) - ord('a')] + po[ord(k[i]) - ord('a')] for i in range(len(s))]
        
        
    
