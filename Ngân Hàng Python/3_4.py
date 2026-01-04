
for _ in range(int(input())):
    s1, s2 = input().split(), input().split()
    if len(s1) != len(s2): print("INVALID")
    else:
        i = set(s1) & set(s2)
        u = set(s1) | set(s2)
        print(f"{(len(i) / len(u)):.5f}")