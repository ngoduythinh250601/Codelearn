def basicEquationMaker(nums):
    ope = "+-*/%"
    n = len(nums)
    for i in range(1, n):
        for j in range(i + 1, n):
            for o in ope:
                try:
                    s = nums[:i] + o + nums[i:j] + "=" + nums[j:]
                    if eval(s.replace("=", "==")) == True:
                        return s
                except:
                    pass
    return "Not possible"
