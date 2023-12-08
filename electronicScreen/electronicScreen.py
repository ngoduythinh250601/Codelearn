def electronicScreen(s):
    num = [
        "01011111",
        "00000101",
        "01110110",
        "01110101",
        "00101101",
        "01111001",
        "01111011",
        "01000101",
        "01111111",
        "01111101",
    ]
    ans = ""
    for i in range(len(s) // 8):
        ans += str(num.index(s[i * 8 : (i + 1) * 8]))
    return ans
