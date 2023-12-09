def prefix_of_word(s, p):
    for i, word in enumerate(s.split()):
        if word.startswith(p):
            return i + 1
    return -1
