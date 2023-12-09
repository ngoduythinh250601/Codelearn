def rounding(n, m):
    r = n % m
    return n if r * 2 == m else n // m * m if r * 2 < m else (n // m + 1) * m
