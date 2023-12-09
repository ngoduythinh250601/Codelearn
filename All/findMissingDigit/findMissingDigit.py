def findMissingDigit(expression):
    digits = "0123456789"
    for i in digits:
        if i not in expression:
            s = expression.replace("X", i)
            s1, s2 = s.split("=")
            if eval(s1) == eval(s2):
                return int(i)
