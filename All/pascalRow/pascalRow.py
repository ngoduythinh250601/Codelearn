def pascalRow(n):
    ans = [1]
    for i in range(n):
        ans.append(0)
        for i in range(len(ans) - 1, 0, -1):
            ans[i] += ans[i - 1]
    return ans
