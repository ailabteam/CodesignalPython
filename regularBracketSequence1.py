def regularBracketSequence1(s):
    res = 0
    for i in range(len(s)):
        if s[i] == '(':
            res += 1
        else:
            res -= 1
        if res < 0:
            return False
    if res:
        return False
    return True
