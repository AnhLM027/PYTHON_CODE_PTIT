
for _ in range(int(input())):
    s1, s2 = input().split(), input().split()
    if len(s1) != len(s2):
        print("INVALID")
    else:
        a, b = list(map(int, s1)), list(map(int, s2))
        res = 0
        for i in range(len(a)): res += abs(a[i] - b[i])
        print(f"{res:.5f}")