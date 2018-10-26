def splitByValue(k, elements):
    rs = []
    for i in elements:
        if i < k:
            rs = rs + [i]
    for i in elements:
        if i >= k:
            rs = rs + [i]
    return rs
