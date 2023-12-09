def longestSubstr(s):
    n = len(s)
    if s.count(s[0]) == n:
        return 0
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return n
    return n - 1
