def interestingNumber(n):
    return 2 ** ("{:b}".format(n).count("0")) % 1000000007
