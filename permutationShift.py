def permutationShift(p):
    mnShift = 0
    mxShift = 0
    for i in range(len(p)):
        if p[i] - i > mxShift:
            mxShift = p[i] - i
        if p[i] - i < mnShift:
            mnShift = p[i] - i
    return mxShift - mnShift
