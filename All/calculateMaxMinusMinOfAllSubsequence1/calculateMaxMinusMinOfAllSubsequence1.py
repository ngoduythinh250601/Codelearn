def calculateMaxMinusMinOfAllSubsequence1(a):
    n, ans = len(a), 0
    for i in range(n):
        for j in range(i, n):
            ans += max(a[i : j + 1]) - min(a[i : j + 1])
    return ans
