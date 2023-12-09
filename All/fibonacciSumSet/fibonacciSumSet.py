def fibonacciSumSet(n):
    f = [0, 1]
    while f[-1] < n:
        f.append(f[-1] + f[-2])
    ans, i = [], len(f) - 1
    while n > 0:
        if n >= f[i]:
            n -= f[i]
            ans.append(f[i])
        i -= 1
    return sorted(ans)
