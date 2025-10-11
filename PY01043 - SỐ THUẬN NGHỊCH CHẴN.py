
a = ['0', '2', '4', '6', '8']
res = []

def sinh(sz, s:str):
    if len(s) * 2 > sz: return
    if s != "" and s[0] == '0': return
    if s:
        res.append(int(s + s[::-1]))
    for c in a:
        sinh(sz, s + c)

sinh(6, "")
res = sorted(res)

def main():
    n = int(input())
    print(' '.join(str(x) for x in res if x < n))

for tc in range(int(input())):
    main()