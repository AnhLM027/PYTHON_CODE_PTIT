
def solve(n: int):
    global cnt
    cnt = 0
    if cnt == 1000: return -1
    cnt += 1
    if(n % 7 == 0): return n
    return solve(n + int(str(n)[::-1]))

def main():
    n = int(input())
    print(solve(n))

for tc in range(int(input())):
    main()