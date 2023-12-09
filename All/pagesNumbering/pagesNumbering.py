def pagesNumbering(n):
    ans = 0
    base, num = 1, 1
    while base * 10 <= n:
        ans += 9 * base * num
        num += 1
        base *= 10
    ans += (n - base + 1) * num
    return ans
