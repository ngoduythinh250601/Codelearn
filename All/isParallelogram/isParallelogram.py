def isParallelogram(arr):
    arr.sort()
    return arr[0] == arr[1] and arr[2] == arr[3] and sum(arr) == 360 and arr[0] > 0
