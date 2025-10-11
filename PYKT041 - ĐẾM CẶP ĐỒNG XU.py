
n = int(input())

a = []
for i in range(n):
    a.append(input())

cot, hang = [0] * n, [0] * n
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            cot[j] += 1
            hang[i] += 1

ans = 0
for i in range(n):
    ans += cot[i] * (cot[i] - 1) / 2 + hang[i] * (hang[i] - 1) / 2
print(int(ans))
    
