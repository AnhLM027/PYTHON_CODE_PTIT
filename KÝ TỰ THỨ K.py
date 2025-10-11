  

def main():
    n, k = map(int, input().split())
    cnt = 1
    while k % 2 == 0:
        cnt += 1
        k //= 2
    print(chr(65 + cnt - 1))

for tc in range(int(input())):
    main()