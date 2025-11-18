
class KH:
    def __init__(self, id, name, type, st, en):
        self.id = f"KH{id:02d}"
        self.name = name
        self.type = type
        self.st = st
        self.en = en
        
        dinhMuc = {"A": 100, "B":500, "C": 200}
        sodien = en - st
        dm = dinhMuc[self.type]
        
        if sodien >= dinhMuc[self.type]:
            self.trongDm = dm * 450
            self.ngoaiDm = (sodien - dm) * 1000
            self.vat = self.ngoaiDm / 20
        else:
            self.trongDm = sodien * 450
            self.ngoaiDm = 0
            self.vat = 0
        
        self.total = self.trongDm + self.ngoaiDm + self.vat
        
    def __str__(self):
        return f"{self.id} {self.name}{int(self.trongDm)} {int(self.ngoaiDm)} {int(self.vat)} {int(self.total)}"
        
        
def chuanhoa(s):
    arr = s.split()
    t = ""
    for w in arr:
        t += w[0].upper() + w[1:].lower() + " "
    return t
        
n = int(input())
a = []

for i in range(n):
    name = chuanhoa(input())
    type, st, en = input().split()
    a.append(KH(i + 1, name, type, int(st), int(en)))
    
for kh in sorted(a, key=lambda x: (-x.total)):
    print(kh)