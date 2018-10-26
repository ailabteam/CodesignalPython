def reflectString(s):
    res = []
    for i in range(len(s)):
        c = ord('z') - ord(s[i])
        newC = chr(c + ord('a'))
        res.append(newC)
    return ''.join(res)