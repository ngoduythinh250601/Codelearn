base = pow(10, 9) + 7


def bitStrings(n):
    if n == 1:
        return 2
    return (
        bitStrings(n // 2) ** 2 % base
        if n % 2 == 0
        else bitStrings(n // 2) ** 2 * 2 % base
    )
