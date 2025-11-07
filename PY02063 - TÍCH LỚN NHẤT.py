
n = int(input())
a = map(int, input().split())

min1 = min2 = min3 = 1001
max1 = max2 = max3 = -1001
for x in a:
    if min1 >= x:
        min3 = min2
        min2 = min1
        min1 = x
    elif min2 >= x:
        min3 = min2
        min2 = x
    elif min3 >= x:
        min3 = x
    
    if max1 <= x:
        max3 = max2
        max2 = max1
        max1 = x
    elif max2 <= x:
        max3 = max2
        max2 = x
    elif max3 <= x:
        max3 = x
        
print(max(max1 * max2 * max3, min1 * min2 * max1))