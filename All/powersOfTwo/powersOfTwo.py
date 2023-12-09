def powersOfTwo(k, arr):
    for i in range(k + 1):
        if pow(2, i) not in arr:
            return pow(2, i)
