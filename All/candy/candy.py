def candy(n, a):
    dd = [0] * (n + 1)
    for x in a:
        dd[x] = 1
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                dd[i] = 1
    for i in range(1, n + 1):
        if dd[i] == 0:
            return i
    return 0
