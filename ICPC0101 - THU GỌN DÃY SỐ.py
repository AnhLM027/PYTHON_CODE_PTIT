n = int(input())
a = input().split()

b = []
for num in a:
    if(len(b) > 0 and (b[-1] + int(num)) % 2 == 0):
        b.pop()
    else:
        b.append(int(num))

print(len(b))


