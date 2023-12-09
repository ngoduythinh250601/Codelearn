def maximumInSlidingWindow(a, k):
    n = len(a)
    from collections import deque

    dq, ans = deque(), []
    for i in range(n):
        while len(dq) > 0 and dq[0][1] <= i - k:
            dq.popleft()
        while len(dq) > 0 and dq[-1][0] <= a[i]:
            dq.pop()
        dq.append([a[i], i])
        ans.append(dq[0][0])
    return ans[k - 1 :]
