def typeOfTriangle(a, b, c):
    a, b, c = sorted([a, b, c])
    if a <= 0:
        return -1
    if a + b <= c:
        return -1
    if a == b == c:
        return 1
    if a == b or b == c or a == c:
        return 2
    if c**2 == a**2 + b**2:
        return 3
    return 0
