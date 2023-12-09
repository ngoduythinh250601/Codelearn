def last_digit(a, b):
    if b == 1:
        return a % 10
    if b == 0:
        return 1
    return (last_digit(a, b // 2) ** 2 * (1 if b % 2 == 0 else a % 10)) % 10
