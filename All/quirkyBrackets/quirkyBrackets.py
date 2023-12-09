def quirkyBrackets(s):
    word = s.split()
    l, r = 0, len(word) - 1
    while l < r:
        if l < r:
            word[l] = "(" + word[l]
            word[r] = ")" + word[r]
            l += 1
        if l < r:
            word[l] = "(" + word[l]
            word[r] = ")" + word[r]
            r -= 1
    return "".join(word)
