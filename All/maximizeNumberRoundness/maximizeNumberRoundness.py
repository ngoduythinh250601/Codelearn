def maximizeNumberRoundness(n):
    st = str(n)
    d = 0
    st = st.rstrip("0")
    while st.count("0") > 0:
        st = st[0 : st.find("0")] + st[-1] + st[st.find("0") + 1 : len(st) - 1]
        st = st.rstrip("0")
        d += 1
    return d
