
n = int(input())
a = list(map(int, input().split()))

ind, ans = 0, 1e9
for i in range(n):
    sum = 0
    for j in a: sum += abs(a[i] - j)
    if sum < ans:
        ans = sum
        ind = i

print(ans, a[ind])