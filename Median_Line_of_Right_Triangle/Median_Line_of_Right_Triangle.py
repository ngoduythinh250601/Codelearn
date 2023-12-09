def medianLine(a):
    if a[0] <= 0 or a[1] <= 0 or a[2] <= 0:
        return 0
    b = sorted(a)
    return b[2] / 2 if b[0] ** 2 + b[1] ** 2 == b[2] ** 2 else 0
