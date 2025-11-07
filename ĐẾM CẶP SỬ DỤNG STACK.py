
n = int(input())
a = [int(input()) for _ in range(n)]

st = []
res = 0

for x in a:
    cnt = 1
    while st and st[-1][0] < x:
        res += st[-1][1]
        st.pop()
        
    if st and st[-1][0] == x:
        res += st[-1][1]
        cnt = st[-1][1] + 1
        st.pop()
        
    if st: res += 1
    st.append((x, cnt))

print(res)
