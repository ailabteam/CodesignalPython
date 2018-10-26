def smallestCyclicString(inputString):

    P = 997
    M = 28001
    prefixHash = []
    powP = []

    def buildHash(s):
        prefixHash.append(0)
        powP.append(1)
        for i in range(1, len(s) + 1):
            prefixHash.append((prefixHash[i - 1] * P + ord(s[i - 1])) % M)
            powP.append((powP[i - 1] * P) % M)

    # Hash of substring with indices [l, r)
    def substrHash(l, r):
        return (prefixHash[r] - (prefixHash[l] * powP[r - l] % M) + M) % M

    n = len(inputString)
    inputString += inputString
    buildHash(inputString)
    bestShift = 0
    for i in range(1, n):
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) / 2
            if (substrHash(bestShift, bestShift + m) ==
                    substrHash(i, i + m)):
                l = m
            else:
                r = m

        commonPrefixLen = l
        if (inputString[bestShift + commonPrefixLen] >
                inputString[i + commonPrefixLen]):
            bestShift = i

    return inputString[bestShift : bestShift + n]
