base = int(1e9 + 7)


def calc(x):
    if x == 1:
        return 2
    return (calc(x // 2) ** 2 * (2 if x % 2 == 1 else 1)) % base


def sumOfPowersTwo(n):
    return calc(n + 1) - 1
