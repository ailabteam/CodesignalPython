def isoscelesTriangle(sides):

    sides.sort()
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return True
    return False

