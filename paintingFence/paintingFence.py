def paintingFence(n, k):
    if n == 1:
        return k
    base = int(1e9 + 7)
    d1, d2 = k, k * k
    for i in range(n - 2):
        d1, d2 = d2, ((d1 + d2) * (k - 1)) % base
    return d2
