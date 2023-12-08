def isMAC48Address(inputString):
    import re

    pattern = re.compile("^([0-9A-F]{2}-){5}[0-9A-F]{2}$")
    return pattern.match(inputString) != None
