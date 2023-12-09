def fileNaming(names):
    ans = []
    for i in range(len(names)):
        cnt = 0
        s = names[i]
        while s in ans:
            cnt += 1
            s = names[i] + "(" + str(cnt) + ")"
        ans.append(s)
    return ans
