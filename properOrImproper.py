def properOrImproper(a):

    if abs(float(a[1]) / a[0]) > 1:
        return 'Proper'
    return 'Improper'
