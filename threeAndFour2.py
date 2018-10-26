def threeAndFour(n):
    result = []
    for counter in range(n):
        if counter % 3 == 0 and counter % 4 == 0:
            result.append( counter )
    return result
