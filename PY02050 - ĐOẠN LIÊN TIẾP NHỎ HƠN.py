
def main():
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    for i in range(0, len(a), 1):
        if len(st) == 0:
            st.append(i)
            print(i + 1, end=' ')
        else:
            while len(st) > 0 and a[i] >= a[st[-1]]:
                st.pop()
            if not st:
                print(i + 1, end=' ')
            else:
                print(i - st[-1], end=' ')
            st.append(i)
    print()

for tc in range(int(input())):
    main()
