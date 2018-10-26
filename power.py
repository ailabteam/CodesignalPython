def power(base, exponent):
    result = 1
    for count in range(exponent):
        result *= base
    return result
