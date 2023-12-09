def regularBracketSequence(sequence):
    cnt = 0
    for c in sequence:
        cnt += 1 if c == "(" else -1
        if cnt < 0:
            return False
    return cnt == 0
