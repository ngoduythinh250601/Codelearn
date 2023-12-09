def evenNumbers(n, p):
    b = 1 << n
    p //= b
    if p == 0:
        return -1
    elif p % 2 == 0:
        return b * (p - 1)
    else:
        return b * p
