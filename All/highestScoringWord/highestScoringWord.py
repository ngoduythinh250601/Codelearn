def high_scoring_word(x):
    ans, highest = "", 0
    for word in x.split():
        current = 0
        for char in word:
            current += ord(char) - ord("a") + 1
        if current > highest:
            highest = current
            ans = word
    return ans
