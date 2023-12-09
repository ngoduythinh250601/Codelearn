def minConvert(n, m):
    if n == 0 and m > 0:
        return -1
    ans = 0
    while m != n:
        ans += 1
        if m > n and m % 2 == 0:
            m /= 2
        else:
            m += 1
    return ans
