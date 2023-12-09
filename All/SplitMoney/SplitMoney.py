def splitMoney(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    arr.append(arr[-1] + 1)
    ans, cnt = 0, 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            ans = max(ans, cnt)
            cnt = 1
        else:
            cnt += 1
    return ans
