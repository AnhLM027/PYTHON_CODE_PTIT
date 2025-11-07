
def solve(index, s):
    if index == n:
        if eval(s) == M:
            results.append(s)
        return
    num = str(a[index]) if a[index] >= 0 else "(" + str(a[index]) + ")"
    solve(index+1, s + "+" + str(num))
    solve(index+1, s + "-" + str(num))
    solve(index+1, s + "*" + str(num))

n, M = map(int, input().split())
a = list(map(int, input().split()))
results = []

first = str(a[0])
if a[0] < 0:
    first = "(" + first + ")"

solve(1, first)

if results:
    for r in results:
        print(f"{r}={M}")
else:
    print("IMPOSSIBLE")
