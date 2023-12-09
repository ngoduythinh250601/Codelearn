def min_max(n):
    s = [i for i in str(n)]
    s.sort()
    h = int("".join(s))
    s.sort(reverse=True)
    k = int("".join(s))
    return k - h
