def isMAC48Address(inputString):
    t = inputString.split('-')
    for x in t:
        if(len(x) != 2):
            return False
        if f(x[0]) == False or f(x[1]) == False:
            return False
    return True
def f(x):
    if (x >= '0' and x <= '9') or (x >= 'A' and x <= 'F'):
        return True
    return False