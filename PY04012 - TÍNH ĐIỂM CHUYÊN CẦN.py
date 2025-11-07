
class SV:
    def __init__(self, msv, name, lop):
        self.msv = msv
        self.name = name
        self.lop = lop
        self.cc = 10
        self.type = ''
        
    def update(self, s):
        for c in s:
            if c == 'v': self.cc -= 2
            if c == 'm': self.cc -= 1
        if self.cc <= 0:
            self.cc = 0
            self.type = "KDDK"
        
    def __str__(self):
        return f"{self.msv} {self.name} {self.lop} {self.cc} {self.type}"
    
n = int(input())
a = {}
for i in range(n):
    msv = input()
    a[msv] = SV(msv, input(), input())
    
for i in range(n):
    msv, s = map(str, input().split())
    a[msv].update(s)

res = list(a.values())
for sv in res:
    print(sv)