def palindromeRearranging(s):
    c = 0
    t = [0 for i in range(26)]
    for i in range(len(s)):
      t[ord(s[i]) - ord('a')] += 1
    for i in t:
      if i % 2 == 1:
        c += 1
    return c == 0 or (c == 1 and len(s) % 2 == 1)