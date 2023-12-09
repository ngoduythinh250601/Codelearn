def marathon_ranking(ranking, scores):
    ranking.append(int(1e8))
    ranking = sorted(set(ranking), reverse=True)
    ans = []
    for x in scores:
        l, r = 0, len(ranking) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if ranking[mid] >= x:
                l = mid
            else:
                r = mid - 1
        ans.append(r + (0 if ranking[r] == x else 1))
    return ans
