def maxLenSubStr(str):
    ans = 0
    for c in range(ord("a"), ord("z") + 1):
        ans = max(ans, str.rfind(chr(c)) - str.find(chr(c)) + 1)
    return ans
