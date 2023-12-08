def groupedBits(n):
    return len(("{:b}".format(n).replace("0", " ")).split())
