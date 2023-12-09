def diagonalLine(arr):
    n = len(arr)
    if n < 2:
        return "-1"
    for i in arr:
        if len(i) != n:
            return "-1"

    return (
        "".join(arr[i][i] for i in range(n))
        + " "
        + "".join(arr[i][n - i - 1] for i in range(n))
    )
