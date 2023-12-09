def onesAndZeros4(s):
    ss = [c for c in s]
    ans = 0
    for i in range(1, len(ss) - 1):
        if ss[i] == "1" and ss[i - 1] == ss[i + 1] == "0":
            ans += 1
            ss[i + 1] = "1"
    return ans
