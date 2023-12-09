def firstMultiple(divisors, start):
    from math import gcd

    x = divisors[0]
    for i in range(1, len(divisors)):
        x = x * divisors[i] // gcd(x, divisors[i])
    return x * (start // x + (1 if start % x > 0 else 0))
