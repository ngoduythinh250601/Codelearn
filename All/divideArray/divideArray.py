def divideArray(a, b):
    from math import gcd

    try:
        b_lcm = b[0]
        for x in b:
            b_lcm = b_lcm * x // gcd(b_lcm, x)
        return sum([x % b_lcm == 0 for x in a])
    except:
        return 0
