def calc(a, b):
    if b == 1:
        return a % 100
    return (calc(a, b // 2) ** 2 * (a % 100 if b % 2 == 1 else 1)) % 100


def lastTwoDigits(a, b):
    return str(calc(a, b)).zfill(2)
