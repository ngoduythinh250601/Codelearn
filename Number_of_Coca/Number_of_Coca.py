def numCoca(x, y):
    ans = x
    while True:
        ans += x // y
        x = x % y + x // y
        if x < y:
            break
    return ans
