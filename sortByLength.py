def sortByLength(a):

    for i in range(len(a)):
        minIndex = i
        tmp = a[i]
        for j in range(i + 1, len(a)):
            if len(a[j]) < len(a[minIndex]):
                minIndex = j
        a[i] = a[minIndex]
        a[minIndex] = tmp

    return a
