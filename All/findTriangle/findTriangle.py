def find_triangle(arr):
    arr.sort()
    return arr[2] if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2 and arr[0] > 0 else -1
