def isSum(value):
    for i in range(1, 400):
        if (i * (i+1) == 2 * value):
            return True
    return False
