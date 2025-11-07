

n = int(input())

freq = {}
for _ in range(n - 1):
    a, b = map(int, input().split())
    freq[a] = freq.get(a, 0) + 1
    freq[b] = freq.get(b, 0) + 1
    
cnt = n - 1
check = False
for num, f in freq.items():
    if f == cnt: check = True
    
print("Yes" if check else "No")