def variableName(name):
    t = name.replace("&quot;", "")
    print t
    ok = True
    if '0' <= t[0] <= '9':
        return False
    for i in range(len(t)):
        if not ('0' <= t[i] <= '9' or 'a' <= t[i] <= 'z' or 'A' <= t[i] <= 'Z' or t[i] == '_'):
            return False
    return True
