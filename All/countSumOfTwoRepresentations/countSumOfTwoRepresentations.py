def countSumOfTwoRepresentations(n, l, r):
    ans = min(n // 2 - l + 1, r - (n - (n // 2)) + 1)
    return ans if ans > 0 else 0
