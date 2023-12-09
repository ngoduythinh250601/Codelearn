def reverseInParentheses(inputString):
    return eval('"' + inputString.replace("(", '"+("').replace(")", '")[::-1]+"') + '"')
