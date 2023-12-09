def isIPv4Address(inputString):
    try:
        ans = [int(x) < 256 and int(x) >= 0 for x in inputString.split(".")]
    except:
        return False
    return sum(ans) == len(ans) == 4
