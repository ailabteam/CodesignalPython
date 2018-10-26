def minimalMultiple(divisor, lowerBound):
    while True:
        if(lowerBound % divisor != 0):
            lowerBound += 1
        else:
            return lowerBound
