def solOfEquations(k, a, b, c):
    n = k - a - b - c
    return (n + 2) * (n + 1) // 2 if n >= 0 else 0
