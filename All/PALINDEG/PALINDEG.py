def deg(string):
    if len(string) == 1 or string != string[::-1]:
        return 0
    return deg(string[0 : (len(string) + 1) // 2]) + 1
