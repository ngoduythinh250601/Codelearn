def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def gold(n):
    ans = 0
    for i in range(2, n // 2 + 1):
        if isPrime(i) and isPrime(n - i):
            ans += 1
    return ans
