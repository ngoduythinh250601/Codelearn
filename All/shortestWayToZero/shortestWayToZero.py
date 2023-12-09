def shortestWayToZero(n, k):
    ans = 0
    while n > 0:
        ans += n % k + 1
        n //= k
    return ans - 1
