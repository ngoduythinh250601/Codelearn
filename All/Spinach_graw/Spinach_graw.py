def spinackGraw(spinack, t):
    n = len(spinack)
    a = [0] * (n + 1)
    for pair in t:
        a[pair[0]] += 1
        a[pair[1] + 1] -= 1
    addition = 0
    for i in range(n):
        addition += a[i]
        spinack[i] = (spinack[i] + addition) % 2
    return spinack
