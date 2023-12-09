def maximalSquare(matrix):
    if len(matrix) == 0:
        return 0
    n, m, ans = (
        len(matrix),
        len(matrix[0]),
        0 if sum(matrix[0]) == 0 and sum(matrix[:][0]) == 0 else 1,
    )
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:
                matrix[i][j] = (
                    min(matrix[i][j - 1], min(matrix[i - 1][j], matrix[i - 1][j - 1]))
                    + 1
                )
                ans = max(ans, matrix[i][j])
    return ans**2
