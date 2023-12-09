def explosion(s):
    ans = []
    for char in s:
        if char.isupper():
            ans.append(char)
    return "".join(ans) if len(ans) > 0 else "Failed"
