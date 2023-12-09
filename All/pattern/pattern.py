def pattern(i):
    n = 1
    for c in range(2, i + 1):
        n = (n + 1) * 2
    return n
