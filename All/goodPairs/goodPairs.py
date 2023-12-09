def goodPairs(n, m, c):
    ans = 0
    for i in range(1, int(c**0.5) + 1):
        if c % i == 0:
            j = c // i
            if i <= n and j <= m:
                ans += 1
            if i <= m and j <= n and i != j:
                ans += 1
    return ans
