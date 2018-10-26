def maxFraction(numerators, denominators):
    idx = 0
    mx = 0.0
    for i in range(len(numerators)):
        if numerators[i] / denominators[i] > mx:
            print numerators[i] * 1.0 / denominators[i] 
            mx = numerators[i] * 1.0 / denominators[i] 
            idx = i
    return idx