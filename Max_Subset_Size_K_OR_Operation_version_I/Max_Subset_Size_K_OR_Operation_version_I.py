def solve(n, k, a):
    # do giới hạn ai <= 1000 mà k >= 10 nên chọn k hay chọn tất cả đều như nhau
    ans = 0
    for i in a:
        ans |= i
    return ans
