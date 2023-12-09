def sumCandy1(add, n):
    inc = [0] * (n + 1)
    for x in add:
        inc[x[0] - 1] += 1
        inc[x[1]] -= 1
    current, ans = 0, [0] * n
    for i in range(n):
        current += inc[i]
        ans[i] = current
    return ans
