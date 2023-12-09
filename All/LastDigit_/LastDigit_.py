def lastDigit(a, b):
    if b == 1:
        return a
    if b == 0:
        return 1
    return (lastDigit(a, b // 2) ** 2 * (a if b % 2 == 1 else 1)) % 10
