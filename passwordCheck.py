def passwordCheck(s):
    ok1 = False
    ok2 = False
    ok3 = False
    if len(s) >= 5:
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                ok1 = True
            if 'A' <= s[i] <= 'Z':
                ok2 = True
            if '0' <= s[i] <= '9':
                ok3 = True
    if ok1 == True and ok2 == True and ok3 == True:
        return True
    return False
