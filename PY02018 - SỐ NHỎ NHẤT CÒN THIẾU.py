
n, a = int(input()), list(map(int, input().split()))
minn = 0
a.sort()
for i in a:
    if i == minn + 1:
        minn = i
print(minn + 1)
