def plantFlowers(arr, n):
    n_arr = len(arr)
    total = 0
    for i in range(n_arr):
        if (
            arr[i] == 0
            and ((i > 0 and arr[i - 1] == 0) or (i == 0))
            and ((i < n_arr - 1 and arr[i + 1] == 0) or (i == n_arr - 1))
        ):
            total += 1
            arr[i] = 1
    return total >= n
