


def backtrack(n, curr_sum, a, res):
    if curr_sum == n:
        res.append(a.copy())
        return
    
    start = a[-1] if a else n
    for i in range(start, 0, -1):
        if curr_sum + i <= n:
            a.append(i)
            backtrack(n, curr_sum + i, a, res)
            a.pop()
        

def main():
    n = int(input())
    res = []
    backtrack(n, 0, [], res)
    print(len(res))
    for a in res:
        print(f"({' '.join(map(str, a))})", end=' ')
    print()
    
for tc in range(int(input())):
    main()
    