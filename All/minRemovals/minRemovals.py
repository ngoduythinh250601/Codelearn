def minRemovals(arr, k):
    arr.sort()
    n, ans = len(arr), 0
    i, j = 0, 0
    while i < n:
        while j < n and arr[j] <= arr[i] + k:
            j += 1
        ans = max(ans, j - i)
        i += 1
    if ans == n:
        ans = n - 1
    return n - ans
