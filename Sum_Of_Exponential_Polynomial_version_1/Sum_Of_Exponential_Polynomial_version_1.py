def soep(n, k):
    ans, base = 0, pow(10, 9) + 7
    for i in range(1, n + 1):
        ans = (ans + pow(i, k)) % base
    return ans
