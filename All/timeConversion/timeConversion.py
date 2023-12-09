def timeConversion(s, t):
    h, m, se = int(s[0:2]) + (12 if s[-2] == "P" else 0), int(s[3:5]), int(s[6:8])
    if s.startswith("12:00:00"):
        h += 12
    se += t
    m, se = m + se // 60, se % 60
    h, m = h + m // 60, m % 60
    h = h % 24
    return "{:02}:{:02}:{:02}".format(h, m, se)
