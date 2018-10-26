def isMAC48Address(s):
    for i in range(len(s)):
        if i % 3 == 2:
            if s[i] != '-':
                return False
        else:
            sym = s[i]
            if not ('0' <= sym <= '9' or  'A' <= sym <= 'F'):
                return False
    return len(s) ==  17