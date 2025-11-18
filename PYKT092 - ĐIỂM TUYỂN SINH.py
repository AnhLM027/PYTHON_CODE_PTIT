
class SV:
    def __init__(self, id, name, diem, dtoc, kv):
        self.id = f"TS{id:02d}"
        self.name = name
        self.diem = diem
        self.dtoc = dtoc
        self.kv = kv
        
        ut = {1: 1.5, 2:1, 3:0}
        self.diem += ut[self.kv]
        if self.dtoc != "Kinh": self.diem += 1.5
        
        if self.diem >= 20.5: self.type = "Do"
        else: self.type = "Truot"

    def __str__(self):
        return f"{self.id} {self.name} {self.diem:.1f} {self.type}"

def chuanhoa(s):
    arr = s.split()
    res = [(t[0].upper() + t[1:].lower()) for t in arr]
    return ' '.join(res)

n = int(input())
a = []
idx = 1
for i in range(1, n + 1):
    name = chuanhoa(input().strip())
    a.append(SV(i, name, float(input()), input(), int(input())))

a.sort(key=lambda x: (-x.diem, x.id))

for ct in a:
    print(ct)
