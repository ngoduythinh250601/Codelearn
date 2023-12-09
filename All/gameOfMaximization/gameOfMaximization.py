def gameOfMaximization(arr):
    ans = [0] * 3
    for i in range(len(arr)):
        ans[i % 3] += arr[i]
    return min(ans) * 3
