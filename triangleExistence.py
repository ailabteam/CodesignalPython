def triangleExistence(sides):
    if sides[0] + sides[1] > sides[2] and sides[2] + sides[1] > sides[0] and sides[0] + sides[2] > sides[1]:
        return True
    return False
