def secondBiggest(n, a):
    a = set(a)
    if len(a) > 1:
        a.remove(max(a))
    return max(a)
