def taxi(arr):
    cnt = [0] * 5
    for x in arr:
        cnt[x] += 1
    ans = cnt[4] + cnt[2] // 2 + min(cnt[3], cnt[1])
    cnt[2] = cnt[2] % 2
    if cnt[3] > cnt[1]:
        return ans + (cnt[2] == 1) + cnt[3] - cnt[1]
    else:
        x = cnt[2] * 2 + cnt[1] - cnt[3]
        cnt[1] -= cnt[3]
        return ans + x // 4 + (x % 4 > 0)
