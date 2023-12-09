def longestDigitsPrefix(s):
    s += "x"
    for i in range(len(s)):
        if not str(s[i]).isdigit():
            return s[:i]
