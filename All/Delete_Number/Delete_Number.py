def min_number(n, a, b):
    if a == b:
        return "empty"
    st = []
    for c in n:
        while b > 0 and len(st) > 0 and st[-1] > c:
            st.pop()
            b -= 1
        st.append(c)
    while b > 0:
        st.pop()
        b -= 1
    return str(int("".join(st)))
