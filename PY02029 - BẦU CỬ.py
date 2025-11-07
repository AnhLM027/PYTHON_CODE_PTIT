
n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = {}

for x in a:
    freq[x] = freq.get(x, 0) + 1
    
max1 = max2 = 0

for x, f in freq.items():
    if f > max1:
        max2 = max1
        max1 = f
    elif f < max1 and f > max2: max2 = f

index = n + 1
for x, f in freq.items():
    if f == max2 and index > x:
        index = x
if max2 == 0 or index == n + 1:
    print("NONE")
else:
    print(index)