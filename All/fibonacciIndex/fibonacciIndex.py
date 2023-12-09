def fibonacciIndex(n):
    f0, f1, n, i = 0, 1, 0 if n == 1 else 10 ** (n - 1), 0
    while True:
        if f0 >= n:
            return i
        f0, f1, i = f1, f0 + f1, i + 1
