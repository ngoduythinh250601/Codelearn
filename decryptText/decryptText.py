def decryptText(s):
    rmd = 0
    ans = []
    for char in s:
        c = chr(ord(char) - rmd + (26 if ord(char) - 97 < rmd else 0))
        ans.append(c)
        rmd = (rmd + ord(c) - 97) % 26
    return "".join(ans)
