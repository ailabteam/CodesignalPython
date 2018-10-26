def oddNumbersBeforeZero(sequence):
    count = 0
    for n in sequence:
        if n == 0:
            break
        if n % 2 == 1:
            count += 1
    return count
