def isMonotonous(sequence):
    if len(sequence) == 1:
        return True
    elif len(sequence) == 2:
        return sequence[0] != sequence[1]
    else:
        for i in range(2, len(sequence)):
            if (sequence[i - 1] - sequence[i - 2]) * (
                sequence[i] - sequence[i - 1]
            ) <= 0:
                return False
        return True
