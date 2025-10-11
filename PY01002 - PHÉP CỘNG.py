
def main():
    s = input().strip()
    vt, sum = s.split('=')
    a , b = vt.split('+')
    if int(a) + int(b) == int(sum):
        print('YES')
    else:
        print('NO')

main()