def maxSumSegments(inputArray):
    res = [0 for i in range(len(inputArray))]
    for i in range(1, len(inputArray) + 1):
        sum = 0
        mxSum = 0
        idx = -1
        for j in range(len(inputArray)):
            sum += inputArray[j]
            if j >= i:
                sum -= inputArray[j-i]
            if j >= i - 1 and (idx == -1 or sum > mxSum):
                mxSum = sum
                idx = j - i + 1
        res[i-1] = idx
    return res