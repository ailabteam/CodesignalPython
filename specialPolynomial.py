def specialPolynomial(x, n):
    curr = 1
    count = 0
    mult = x
    while curr + mult <= n:
        curr += mult
        mult *= x
        count += 1
    return count