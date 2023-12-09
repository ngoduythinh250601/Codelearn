def hard_min_swaps(arr):
    ans = 0
    for i in range(len(arr)):
        while i != arr[i] - 1:
            ot = arr[i]
            arr[i], arr[ot - 1] = arr[ot - 1], arr[i]
            ans += 1
    return ans
