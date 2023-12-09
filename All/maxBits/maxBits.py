def maxBits(n):
    return int("".join(sorted(list("{:b}".format(n)), reverse=True)), 2)
