def getThePassword(key1, key2):
    for leng in range(len(key1), 0, -1):
        for i in range(len(key1) - leng + 1):
            if key1[i : i + leng] in key2:
                return leng
    return 6008009
