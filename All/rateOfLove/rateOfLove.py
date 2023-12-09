def rateOfLove(name):
    s = (name[0] + name[1]).lower().replace(" ", "")
    marked = [0] * 256
    ans = ""
    for c in s:
        if marked[ord(c)] == 0:
            marked[ord(c)] = 1
            ans += str(s.count(c))
    while int(ans) > 100:
        t = ""
        for i in range(len(ans) - 1):
            t += str((int(ans[i]) + int(ans[i + 1])) % 10)
        ans = t
    return int(ans)
