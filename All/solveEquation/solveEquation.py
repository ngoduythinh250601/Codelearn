def s(x):
    return sum([int(c) for c in str(x)])


def solveEquation(n):
    x = int(n**0.5)
    for i in range(min(90, x)):
        if x * x + s(x) * x == n:
            return x
        x -= 1
    return -1
