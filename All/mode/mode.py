def mode(arr):
    arr.sort()
    arr.append(arr[-1] + 1)
    max_cnt, cnt, ans, current_sum = 0, 1, 0, arr[0]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            if cnt > max_cnt:
                ans = current_sum
                max_cnt = cnt
            elif cnt == max_cnt:
                ans += current_sum
            cnt = 1
            current_sum = arr[i]
        else:
            cnt += 1
            current_sum += arr[i]
    return ans
