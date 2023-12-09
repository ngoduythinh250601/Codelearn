def sumOfTwoPowers(n, k):
    ans = []
    p1, p2 = 0, int(n ** (1 / k)) + 2
    while p1 <= p2:
        total = p1**k + p2**k
        if total == n:
            ans.append([p1**k, p2**k])
            p1, p2 = p1 + 1, p2 - 1
        elif total > n:
            p2 -= 1
        else:
            p1 += 1
    return ans
