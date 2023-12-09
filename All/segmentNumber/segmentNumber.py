def segmentNumber(a, segLen):
    a.sort()
    a.append(1000000)
    start, ans = 0, 0
    for i in range(1, len(a)):
        if a[i] > a[start] + segLen:
            start, ans = i, ans + 1
    return ans
