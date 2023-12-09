def numberOfSquares(n):
    return (
        n * (n + 1) ** 3 // 2
        + n**2 * (n + 1) ** 2 // 4
        - 2 * n * (n + 1) ** 2 * (2 * n + 1) // 6
    ) % 1000000007
