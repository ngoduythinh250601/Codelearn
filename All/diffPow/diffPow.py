def diffPow(n):
    a, b = 0, 0
    for i in range(1, n + 1):
        a += i**6
        b += i
    b = b**2
    return (a - b) % 1000000007
