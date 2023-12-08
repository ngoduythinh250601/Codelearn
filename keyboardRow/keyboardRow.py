def keyboardRow(words):
    lines = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    ans = []
    for word in words:
        for line in lines:
            count = 0
            for char in word.lower():
                if char in line:
                    count += 1
            if count == len(word):
                ans.append(word)
    return ans
