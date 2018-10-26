def prefixFunctionNaive(s):

    result = []

    for i in range(len(s)):
        result.append(0)
        for result[i] in range(i, -1, -1):
            matches = True
            for j in range(i - result[i] + 1, i + 1):
                if s[j] != s[j - i + result[i] - 1]:
                    matches = False
                    break
            if matches:
                break

    return result
