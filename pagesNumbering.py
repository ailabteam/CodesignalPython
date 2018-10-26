def pagesNumbering(n):

    tenPower = 1
    digitsPerPage = 1
    result = 0

    while tenPower * 10 <= n:
        result += tenPower * 9 * digitsPerPage
        tenPower *= 10
        digitsPerPage += 1
    result +=  (n - tenPower + 1) * digitsPerPage

    return result
