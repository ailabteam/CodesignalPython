def zFunctionNaive(s):
    r = [0 for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if i + j < len(s) and s[i+j] == s[j]:
                r[i] += 1
            else:
                break
    return r
