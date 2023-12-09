def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def sumDivisors(n):
    ans = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if not isPrime(i):
                ans += i
            if not isPrime(n // i) and n // i != i:
                ans += n // i
    return ans
