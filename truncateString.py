def truncateString(s):
    while len(s) > 0:
        ok = 0
        while len(s) > 0 and int(s[0]) % 3 == 0:
            ok = 1
            s = s[1:]
        print s
        
        while len(s) > 0 and int(s[len(s) - 1]) % 3 == 0:
            ok = 1
            s = s[0:len(s) - 1]
            print s
        print s
        while len(s) > 1 and (int(s[len(s) - 1]) + int(s[0])) % 3 == 0:
            ok = 1
            s = s[1:]
            s = s[0:len(s) - 1]
        print s
        if ok == 0:
            break
    return s
