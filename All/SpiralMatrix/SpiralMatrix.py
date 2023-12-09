def spiralMatrix(n):
    ans = [[0] * n for i in range(n)]
    l, r, k = 0, n - 1, 1
    while k <= n**2:
        if k <= n**2:
            for i in range(l, r + 1):
                ans[l][i] = k
                k += 1
        if k <= n**2:
            for i in range(l + 1, r + 1):
                ans[i][r] = k
                k += 1
        if k <= n**2:
            for i in range(r - 1, l - 1, -1):
                ans[r][i] = k
                k += 1
        if k <= n**2:
            for i in range(r - 1, l, -1):
                ans[i][l] = k
                k += 1
        l += 1
        r -= 1
    return ans
