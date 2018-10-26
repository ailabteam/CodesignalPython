def pointInLine(point, line):
    x, y = point
    if line[0] * x + line[1] * y + line[2] == 0:
        return True
    return False