def countOx(a, k):
    if k == 0:
        return 0
    ans = 0
    for x in a:
        if (x - int(str(x)[::-1])) % k == 0:
            ans += 1
    return ans
