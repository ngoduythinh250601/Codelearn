def sumOfConsecutive(n):
    ans = 0
    n *= 2
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0) and ((n // i - i) % 2 != 0):
            ans += 1
    return ans
