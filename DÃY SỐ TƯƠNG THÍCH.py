
n = int(input())
a = list(map(int,input().split()))
b = [1] * n
while True:
    for i in range(0, n - 1):
        while a[i] // b[i] != a[i + 1] // b[i + 1]:
            if a[i] // b[i] > a[i + 1] // b[i + 1]: b[i] += 1
            else: b[i + 1] += 1
    if a[0] // b[0] == a[n - 2] // b[n - 2]: break
print(sum(b))
