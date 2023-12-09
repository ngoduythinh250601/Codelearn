def encryption(s):
    s = s.replace(" ", "")
    n = len(s)
    col = int(n**0.5) + 1
    ans = []
    for i in range(col):
        ans.append(s[i::col])
    return "".join(ans)
