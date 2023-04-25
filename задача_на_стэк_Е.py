def solve(str):
    st = []
    for w in str:
        if w.isdigit():
            st.append(int(w))
            continue
        x = st.pop()
        y = st.pop()
        res = 0
        if w == '+':
            res += (x + y)
        elif w == '-':
            res += (x - y)
        elif w == '*':
            res += (x * y)
        elif w == '/':
            res += (x // y)
        st.append(res)
    return st.pop()

str = input()
print(solve(str))