
for _ in range(int(input())):
    s1 = input().split()
    s2 = input().split()
    p = int(input())
    if len(s1) != len(s2): print("INVALID")
    else:
        a, b = list(map(int, s1)), list(map(int, s2))
        sum = 0
        for i in range(len(a)): sum += pow(abs(a[i] - b[i]), p)
        
        res = pow(sum, 1 / p)
        print(f"{res:.5f}")