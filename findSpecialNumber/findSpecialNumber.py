def findSpecialNumber(n):
    arr = [1, 2, 2]
    i = 2
    while len(arr) < n:
        i += 1
        arr.extend([i] * arr[i - 1])
    return arr[n - 1]
