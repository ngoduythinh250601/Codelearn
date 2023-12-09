def checkNumber(s):
    try:
        int(s)
        return 1
    except:
        return -1
