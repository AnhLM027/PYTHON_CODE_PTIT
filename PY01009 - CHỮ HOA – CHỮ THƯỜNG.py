
def main():
    s = input()
    cnt = 0
    for c in s:
        if c >= 'A' and c <= 'Z':
            cnt += 1
    if(len(s) - cnt >= cnt):
        print(s.lower())
    else:
        print(s.upper())

main()