def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def sumPrimeIndex(arr):
    return sum(arr[i] if isPrime(i) == True else 0 for i in range(1, len(arr)))
