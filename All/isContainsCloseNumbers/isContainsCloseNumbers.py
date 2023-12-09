def isContainsCloseNumbers(nums, k):
    for i in range(len(nums) - k + 1):
        a = nums[i : i + k + 1]
        if len(set(a)) != len(a):
            return True
    return False
