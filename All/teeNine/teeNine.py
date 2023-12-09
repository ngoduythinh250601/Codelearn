def teeNine(message):
    message = message.upper()
    T9 = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    for i in range(2, 10):
        for c in T9[i]:
            message = message.replace(c, str(i))
    cnt, ans = 0, []
    message = message + "z"
    for i in range(1, len(message)):
        if message[i] != message[i - 1]:
            try:
                j = int(message[i - 1])
                ans.append(T9[j][cnt % len(T9[j])])
            except:
                ans.append(message[i - cnt - 1 : i])
            cnt = 0
        else:
            cnt += 1
    return "".join(ans).lower()
