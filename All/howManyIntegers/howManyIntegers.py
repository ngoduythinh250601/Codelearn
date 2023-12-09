def howManyIntegers(n):
    ans = 0
    for i in range(1, n):
        s = str(i)
        ans += len(s) == s.count("0") + s.count("4") + s.count("7")
    return ans
