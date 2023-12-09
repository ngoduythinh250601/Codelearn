def modifyString(s):
    s += "."
    cnt, ans = 1, 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            cnt += 1
        else:
            ans += (cnt - 1) // 2
            cnt = 1
    return ans
