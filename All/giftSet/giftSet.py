def giftSet(a, b, c, d, e, f):
    bc = min(b, c)
    if a + bc <= d:
        return a * e + bc * f
    elif e > f:
        return a * e + (d - a) * f if a <= d else d * e
    else:
        return bc * f + (d - bc) * e if bc <= d else d * f
