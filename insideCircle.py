def insideCircle(point, center, radius):
    dis = math.sqrt((point[0] - center[0]) * (point[0] - center[0]) + (point[1] - center[1]) * (point[1] - center[1]) )
    return dis <= radius
    
