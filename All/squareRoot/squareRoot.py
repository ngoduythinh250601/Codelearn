def squareRoot(n, m):
    n **= 0.5
    return str(int(n)) + str(float(n) - int(n))[1 : m + 2]
