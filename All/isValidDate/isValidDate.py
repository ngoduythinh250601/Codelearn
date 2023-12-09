def isValidDate(d, m, y):
    if d > 31 or d <= 0 or m > 12 or m <= 0:
        return False
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        months[2] = 29
    return d <= months[m]
