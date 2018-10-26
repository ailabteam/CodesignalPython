def swapCase(s):
    res = ''
    for x in s:
        if 'a' <= x <= 'z':
            res += chr(ord(x) - 32)
        if 'A' <= x <= 'Z':
            res += chr(ord(x) + 32)
    return res
