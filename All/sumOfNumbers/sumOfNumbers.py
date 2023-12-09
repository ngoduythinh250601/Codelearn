def sumOfNumbers(arr, n):
    ans = 0
    for i in range(1, n + 1):
        for devider in arr:
            if i % devider == 0:
                ans += i
                break
    return ans
