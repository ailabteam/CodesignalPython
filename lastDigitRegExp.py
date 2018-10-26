def lastDigitRegExp(s):
    for i in s[::-1]:
        if i.isdigit():
            return i

