def maxDivisor(left, right, divisor):
    if left > right:
        left, right = right, left
    while right >= left:
        if right % divisor == 0:
            return right
        right -= 1
    return -1
