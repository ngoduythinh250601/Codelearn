def steelTempest(ingame):
    cnt, ans = 0, 0
    for stt in ingame:
        if stt == 1:
            cnt += 1
        else:
            ans += (cnt + 1) // 3
            cnt = 0
    return ans + cnt // 3
