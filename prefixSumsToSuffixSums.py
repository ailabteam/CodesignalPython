def prefixSumsToSuffixSums(a):
    for i in reversed(range(1, len(a))):
        a[i] -= a[i-1]
        
    print(a)
        
    for i in range(len(a)-2, -1, -1):
        a[i] += a[i+1]
    return a
