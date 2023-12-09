def maxXOR(l, r):
    ans = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            ans = max(ans, i ^ j)
    return ans
