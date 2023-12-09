def identifyOrder(a):
    b = sorted(a, reverse=True)
    n = len(b)
    for i in range(len(a)):
        a[i] = b.index(a[i]) + 1
    return a
