def cipher26(message):
    ans = []
    carry = 0
    for c in message:
        ans.append(chr((ord(c) - 97 - carry) % 26 + 97))
        carry += ord(c) - 97 - carry
    return "".join(ans)
