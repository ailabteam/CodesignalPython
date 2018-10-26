def isPangram(sentence):
    check = [0 for i in range(26)]
    sentence = sentence.lower()
    for i in range(len(sentence)):
        t = sentence[i]
        if t >= 'a' and t <= 'z':
            check[ord(t) - ord('a')] += 1
    for i in range(26):
        if check[i] == 0:
            return False
    return True
