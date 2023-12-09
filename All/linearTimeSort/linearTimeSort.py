def linearTimeSort(arr):
    n = len(arr)
    cnt = [0] * (n + 1)
    for x in arr:
        cnt[x] += 1
    j = 0
    for i in range(n + 1):
        while cnt[i] > 0:
            arr[j] = i
            j += 1
            cnt[i] -= 1
    return arr
