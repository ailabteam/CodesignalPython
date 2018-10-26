def increaseNumberRoundness(n):
    ok = False
    while n > 0:
        if n % 10 == 0 and ok:
            return True
        elif n % 10 != 0:
            ok = True
        n /= 10
    return False