def lCM(n):
    from math import gcd

    ans = 1
    for i in range(2, n + 1):
        ans = ans * i // gcd(ans, i)
    return ans
