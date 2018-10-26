def symbolsPermutation(word1, word2):
    a = list(word1)
    b = list(word2)
    a.sort()
    b.sort()
    return a == b
