def maxReward(n, k):
    ans = functools.reduce(lambda a, b: math.gcd(a, b), k)
    return ans if ans > 1 else min(k)
