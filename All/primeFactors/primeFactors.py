def primeFactors(n):
    ans = []
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            ans.append(i)
    return ans
