
n = int(input())
a = []

for _ in range(n):
    a.append([input(), list(map(int, input().split()))])
    
for x in sorted(a, key=lambda x: (-x[1][0], -x[1][1], -x[1][2])):
    print(x[0], *x[1])