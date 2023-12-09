def generate_hashtag(s):
    s = s.title().split()
    ans = "#" + "".join(s)
    return ans if 1 < len(ans) <= 140 else "wrong"
