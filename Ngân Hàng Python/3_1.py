from math import sqrt

for _ in range(int(input())):
    s1, s2 = input().split(), input().split()
    if len(s1) != len(s2):
        print("INVALID")
    else:
        a, b = list(map(int, s1)), list(map(int, s2))
        
        res = 0
        for i in range(len(a)): res += (b[i] - a[i]) * (b[i] - a[i])
        print(f"{sqrt(res):.5f}")