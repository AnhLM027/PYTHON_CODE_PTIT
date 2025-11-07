
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    max_val = max(arr)
    
    idx = arr.index(max_val)
    arr.insert(idx, m)
    
    neg = [x for x in arr if x < 0]
    pos = [x for x in arr if x >= 0]
    
    res = neg + pos
    print(*res)