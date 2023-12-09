def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def find_special_prime(n):
    ans = [2, 3, 5, 7]
    i = 0
    while i < len(ans):
        if ans[i] > n:
            break
        for x in [1, 3, 7, 9]:
            if isPrime(ans[i] * 10 + x) == True:
                ans.append(ans[i] * 10 + x)
        i += 1
    return ans[0:i]
