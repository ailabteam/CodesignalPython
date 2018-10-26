def removeDigits(n, k):
    maxi = 0
    mini = 10**k
    for i in range(len(str(n))-k+1):
        x = int(str(n)[i:i+int(k)])
        maxi = max(maxi,x)
        mini = min(mini,x)
    return [mini,maxi]
