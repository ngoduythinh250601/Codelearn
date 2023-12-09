def fiboSum(n):
    fib = [1, 2]
    f1, f2 = 1, 2
    while f2 < n:
        f1, f2 = f2, f1 + f2
        fib.append(f2)
    i, s = len(fib) - 1, sum(fib) - n
    while s > 0:
        if s >= fib[i]:
            s -= fib.pop(i)
        i -= 1
    if s > 0 or n == 0:
        return [-1]
    return fib
