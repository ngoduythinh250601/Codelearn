def leftRigthCipher(s):
    n = len(s)
    ans = ""
    while n > 0:
        if n % 2 == 0:
            ans += s[-1]
            s = s[:-1]
        else:
            ans += s[0]
            s = s[1:]
        n -= 1
    return ans[::-1]
