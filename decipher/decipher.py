def decipher(cipher):
    i = 0
    ans = []
    while i < len(cipher):
        if cipher[i] == "1":
            ans.append(chr(int(cipher[i : i + 3])))
            i += 3
        else:
            ans.append(chr(int(cipher[i : i + 2])))
            i += 2
    return "".join(ans)
