def makeTriangle(a, b, c):
    d = max(a, b, c)
    e = a + b + c - d
    return 0 if d < e else d - e + 1
