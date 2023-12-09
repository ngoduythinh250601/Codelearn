def findGoodNumber(n):
    b3 = []
    while n > 0:
        b3.append(n % 3)
        n //= 3
    b3.append(0)
    pos = 0
    for i in range(len(b3)):
        if b3[i] >= 2:
            b3[i + 1] += 1
            pos = i + 1
    for i in range(pos):
        b3[i] = 0
    ans = 0
    for i in range(len(b3) - 1, -1, -1):
        ans = ans * 3 + b3[i]
    return ans
