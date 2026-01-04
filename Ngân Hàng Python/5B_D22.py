
def genn(s):
    g1 = []
    
    if s[0] == '?':
        for i in range(1, 10): g1.append(str(i) + s[1])
    else: g1.append(s)
    
    g2 = []
    
    if s[1] == '?':
        for t in g1:
            for i in range(0, 10): g2.append(t[0] + str(i))
    else: g2 = g1
    return g2

def geno(s):
    if s == '?': return "+-*/"
    return s

def check(a, o, b, c):
    if o == "+": return a + b == c
    elif o == "-": return a - b == c
    elif o == "*": return a * b == c
    elif a % b == 0: return a //b == c
    return False
    
def solve(s):
    arr = s.split()
    a = genn(arr[0])
    o = geno(arr[1])
    b = genn(arr[2])
    c = genn(arr[4])
    
    for i in a:
        for j in o:
            for k in b:
                for l in c:
                    if check(int(i), j, int(k), int(l)):
                        print(f"{i} {j} {k} = {l}")
                        return
    print("WRONG PROBLEM!")
    
for _ in range(int(input())):
    solve(input())
                        