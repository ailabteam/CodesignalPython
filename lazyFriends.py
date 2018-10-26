def lazyFriends(houses, maxDist):
    result = []
    left = 0
    right = 0
    for i in range(len(houses)):
        while houses[i] - houses[left] > maxDist:
            left += 1
        while right + 1 < len(houses) and houses[right + 1] - houses[i] <= maxDist: 
            right += 1
        result.append(right - left)
    return result
