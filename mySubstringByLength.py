def mySubstringByLength(inputString, start, length):

    result = []
    for i in range(start, start+length):
        result.append(inputString[i])
    return ''.join(result)
