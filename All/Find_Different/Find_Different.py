def findDifferent(str_1, str_2):
    s1, s2 = set(list(str_1)), set(list(str_2))
    a1, a2 = sorted(list(s1 - s2)), sorted(list(s2 - s1))
    if len(a1) == len(a2) == 0:
        return ["-1"]
    ans = []
    if len(a1):
        ans.append("".join(a1))
    if len(a2):
        ans.append("".join(a2))
    return ans
