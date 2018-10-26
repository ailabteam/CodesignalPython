def knapsackLight2(weight1, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return "both"
    elif weight1 <= maxW and weight2 > maxW:
        return "first"
    elif weight2 <= maxW and weight1 > maxW:
        return "second"
    elif weight1 <= maxW and weight2 <= maxW:
        return "either"
    else:
        return "none"
