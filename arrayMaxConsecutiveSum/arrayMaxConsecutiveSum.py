def arrayMaxConsecutiveSum(inputArray, k):
    sumK = [sum(inputArray[i : i + k]) for i in range(len(inputArray) - k + 1)]
    return max(sumK)
