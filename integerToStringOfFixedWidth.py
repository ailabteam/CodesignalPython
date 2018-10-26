def integerToStringOfFixedWidth(number, width):
    return ('0'*width+str(number))[-width:]