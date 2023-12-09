def coolString(inputString):
    if inputString.isalpha() == False:
        return False
    for i in range(1, len(inputString)):
        if inputString[i].islower() + inputString[i - 1].islower() != 1:
            return False
    return True
