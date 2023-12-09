def gameOfMatches(n):
    dd = [False] * (n + 10)
    dd[2] = dd[3] = dd[4] = dd[5] = True
    for i in range(6, n + 1):
        dd[i] = not (dd[i - 2] and dd[i - 3] and dd[i - 5])
    return "Ngoc" if dd[n] else "Phong"
