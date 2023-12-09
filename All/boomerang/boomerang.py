def boomerang(arr):
    ans = 0
    for i in range(2, len(arr)):
        ans += arr[i] == arr[i - 2] and arr[i] != arr[i - 1]
    return ans
