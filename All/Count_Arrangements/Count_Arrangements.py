def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def countArrangements(N):
    nt = 0
    for i in range(1, N + 1):
        nt += isPrime(i)
    ans, base = 1, int(1e9 + 7)
    for i in range(1, nt + 1):
        ans = ans * i % base
    for i in range(1, N - nt + 1):
        ans = ans * i % base
    return ans
