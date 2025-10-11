
def main():
    a = []
    while True:
        try:
            a.extend(map(int, input().split()))
        except: break
    return len({x % 42 for x in a})

# for tc in range(0, int(input())):
print(main())