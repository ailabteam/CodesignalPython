def makeArrayConsecutive2(statues):
    mn = min(statues)
    mx = max(statues)
    return mx - mn - len(statues) + 1
