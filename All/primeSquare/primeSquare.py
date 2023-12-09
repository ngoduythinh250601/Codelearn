def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def primeSquare(n):
    return (
        n * n
        if isPrime(n)
        else sum([i * i if isPrime(i) else i for i in range(1, n + 1)])
    )
