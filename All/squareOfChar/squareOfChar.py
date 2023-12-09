def squareOfChar(s):
    s = s[::-1]
    ans = []
    n = len(s) * 2 - 1
    for i in range(n):
        row = ""
        r_min = min(i, n - i - 1)
        for j in range(n):
            pos = min(r_min, min(j, n - j - 1))
            row += s[pos]
        ans.append(row)
    return ans
