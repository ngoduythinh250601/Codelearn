def makeDigitsZero(n):
    ans = 0
    while n > 0:
        n -= int(max(str(n)))
        ans += 1
    return ans
