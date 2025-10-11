
class SV:
    def __init__(self, name, accept, submit):
        self.name = name
        self.accept = accept
        self.submit = submit
        
n = int(input())

a = []
for _ in range(n):
    name = input()
    acc, sub = map(int, input().split())
    a.append(SV(name, acc, sub))

a = sorted(a, key = lambda x: (-x.accept, x.submit, x.name))
for sv in a: print(sv.name, sv.accept, sv.submit)

