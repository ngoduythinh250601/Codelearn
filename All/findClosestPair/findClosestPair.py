def findClosestPair(numbers, sum):
    ans = 1000
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                ans = min(ans, j - i)
    return ans if ans < 1000 else -1
