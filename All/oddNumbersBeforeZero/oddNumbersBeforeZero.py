def oddNumbersBeforeZero(sequence):
    ans = 0
    for i in range(sequence.index(0)):
        if sequence[i] % 2 == 1:
            ans += 1
    return ans
