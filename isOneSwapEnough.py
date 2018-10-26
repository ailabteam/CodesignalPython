def isOneSwapEnough(s):
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            a = list(s)
            a[j] = s[i]
            a[i] = s[j]
            if f(a):
                return 1
    return 0

def f(s):
        return s == s[::-1]