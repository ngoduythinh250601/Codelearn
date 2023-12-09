def divisible_by_senven(n, m):
    return ", ".join([str(i) for i in range(n, m + 1) if i % 7 == 0 and i % 5 != 0])
