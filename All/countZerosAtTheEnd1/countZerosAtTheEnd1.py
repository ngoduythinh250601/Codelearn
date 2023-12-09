def countZerosAtTheEnd1(n):
    ans, mul = 0, 1
    for i in range(n, 0, -2):
        mul *= i
        while mul % 10 == 0:
            mul //= 10
            ans += 1
        mul = mul % 10000000
    return ans
