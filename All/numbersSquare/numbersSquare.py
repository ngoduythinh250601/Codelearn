def numbersSquare(n, s):
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i):
            a[j][i] = s
            s += 1
        for j in range(i, -1, -1):
            a[i][j] = s
            s += 1
    return a
