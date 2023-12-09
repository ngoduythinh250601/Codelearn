def twinSquares2(n):
    ans = (n * 2 + 1) ** 2 // 2
    return [ans**2, (ans + 1) ** 2]
