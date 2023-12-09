def maxIncreaseSubArray(arr):
    ans, cr, pre = 1, 1, arr[0]
    for i in range(1, len(arr)):
        cr = 1 + cr if arr[i] > pre else 1
        pre = arr[i]
        ans = max(ans, cr)
    return ans
