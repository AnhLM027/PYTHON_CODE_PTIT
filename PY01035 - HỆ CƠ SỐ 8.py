
n = input()

while len(n) % 3 != 0: n = "0" + n
ans = ""

for i in range(0, len(n), 3):
    sum = 0
    for j in range(3): sum = sum * 2 + int(n[i + j])
    ans += str(sum)

print(ans)
