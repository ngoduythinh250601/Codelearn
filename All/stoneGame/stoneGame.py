def stoneGame(n):
    dd = [False] * (n + 1)
    s = [1]
    for a in range(2, int(n**0.5) + 1):
        x = a**2
        while x <= n:
            s.append(x)
            x *= a
    s = list(set(s))
    s.sort()
    for i in range(n):
        for x in s:
            if i + x > n:
                break
            dd[i + x] = dd[i + x] or not dd[i]

    return 1 if dd[n] else 2
