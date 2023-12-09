def timeCalculation(s):
    return "{:02}:{:02}:{:02}".format(s // 3600, s % 3600 // 60, s % 60)
