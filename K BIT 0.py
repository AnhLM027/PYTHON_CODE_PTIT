
def init():
    C = [[0]*40 for _ in range(40)]
    for i in range(34):
        C[i][0] = 1
        for j in range(1, i+1):
            C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C

def get(pos, s0, a, C):
    if pos == 0:
        return 1 if s0 == 0 else 0
    res = 0
    if a[pos]:
        if pos < a[0] and s0 > 0: res = C[pos-1][s0-1]
        res += get(pos-1, s0, a, C)
    else:
        if s0 > 0: res = get(pos-1, s0-1, a, C)
    return res

def solve(n, k, C):
    a = [0]*40
    tmp = n
    while tmp:
        a[0] += 1
        a[a[0]] = tmp & 1
        tmp >>= 1

    if k > a[0]:
        print(0)
        return

    res = get(a[0], k, a, C)
    for l in range(1, a[0]): res += C[l-1][k]
    if k == 1: res += 1
    print(res)

C = init()

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 0: print(1 if k == 1 else 0)
    else: solve(n, k, C)
