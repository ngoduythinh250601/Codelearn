def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def detachedSemiPrime(n):
    if n < 2:
        return [-1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and isPrime(i) and isPrime(n // i):
            return [i, n // i]
    return [-1]
