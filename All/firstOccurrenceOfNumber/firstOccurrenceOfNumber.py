def firstOccurrenceOfNumber(n):
    s = "0"
    for i in range(1, n + 1):
        s += str(i)
    return s.find(str(n))
