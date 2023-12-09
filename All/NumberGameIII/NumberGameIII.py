def numberGameIII(s):
    from math import gcd
    from functools import reduce

    x = reduce(lambda a, b: gcd(a, b), s)
    return x if x in s else -1
