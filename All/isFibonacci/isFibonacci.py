def isFibonacci(k):
    a, b = (5 * k**2 + 4) ** 0.5, (5 * k**2 - 4) ** 0.5
    return a.is_integer() or b.is_integer()
