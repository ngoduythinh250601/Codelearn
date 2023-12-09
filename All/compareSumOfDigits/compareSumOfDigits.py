def compareSumOfDigits(input):
    ans = 0
    for c in input:
        v = int(c)
        ans += v if v % 2 == 1 else -v
    return ans
