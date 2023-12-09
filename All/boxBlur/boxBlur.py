def boxBlur(image):
    n, m = len(image), len(image[0])
    for i in range(n):
        for j in range(m):
            image[i][j] = (
                image[i][j]
                + (image[i][j - 1] if j > 0 else 0)
                + (image[i - 1][j] if i > 0 else 0)
                - (image[i - 1][j - 1] if i > 0 and j > 0 else 0)
            )
    n, m = n - 2, m - 2
    ans = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = (
                image[i + 2][j + 2]
                - (image[i + 2][j - 1] if j > 0 else 0)
                - (image[i - 1][j + 2] if i > 0 else 0)
                + (image[i - 1][j - 1] if i > 0 and j > 0 else 0)
            ) // 9
    return ans
