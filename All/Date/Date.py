def date(d, m):
    dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = 3
    while m > 1:
        m -= 1
        d += dom[m - 1]
    return dow[(d + start - 1) % 7]
