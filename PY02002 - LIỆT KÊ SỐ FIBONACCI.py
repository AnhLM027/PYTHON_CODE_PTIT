
f = [0] * 93
f[0], f[1] = 0, 1
for i in range(2, 93):
    f[i] = f[i - 1] + f[i - 2]

def main():
    a, b = map(int, input().split())
    for i in range(a, b + 1): print(f[i], end=' ')
    print()

for tc in range(0, int(input())):
    main()