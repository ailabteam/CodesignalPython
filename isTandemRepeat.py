def isTandemRepeat(inputString):
    print inputString[:len(inputString)/2] 
    print inputString[len(inputString)/2:]
    return inputString[:len(inputString)/2] == inputString[len(inputString)/2:]
