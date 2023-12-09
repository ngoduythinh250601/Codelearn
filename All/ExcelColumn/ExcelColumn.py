def numToName(ColNumber):
    ans = ""
    while ColNumber > 0:
        x = ColNumber % 26
        ans += chr(64 + x if x > 0 else 26)
        ColNumber //= 26
    return ans[::-1]
