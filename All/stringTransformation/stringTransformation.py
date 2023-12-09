def stringTransformation(s):
    cnt, ans = dict(), 0
    for c in s:
        cnt[c] = cnt.get(c, 0) + 1
    num_list = "zero two six seven four three five eight one nine".split()
    key_list = "z w x s u r f t o i".split()
    value_list = [0, 2, 6, 7, 4, 3, 5, 8, 1, 9]
    for i in range(10):
        tmp = cnt.get(key_list[i], 0)
        ans += tmp * value_list[i]
        for c in num_list[i]:
            cnt[c] = cnt.get(c, 0) - tmp
    return ans
