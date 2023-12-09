def cyclicSequence(sequence):
    sequence.append(sequence[0])
    cnt = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            cnt += 1
    return cnt <= 1
