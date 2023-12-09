def fibonacciNumber(n):
    if n == 0:
        return 0
    f0, f1, mod = 0, 1, int(1e9 + 7)
    for i in range(2, n + 1):
        f0, f1 = f1, (f0 + f1) % mod
    return f1
