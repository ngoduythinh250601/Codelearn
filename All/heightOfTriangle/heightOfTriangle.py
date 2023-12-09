def heightOfTriangle(n):
    ans = int((n * 2) ** 0.5)
    return ans if ans * (ans + 1) // 2 <= n else ans - 1
