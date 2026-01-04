
class NV:
    def __init__(self, id, name, vao, ra):
        self.id = id
        self.name = name
        m1 = int(vao[:2]) * 60 + int(vao[3:])
        m2 = int(ra[:2]) * 60 + int(ra[3:])
        
        self.time = m2 - m1 - 60
        self.h = self.time // 60
        self.m = self.time % 60
        self.type = "DU" if self.h >= 8 else "THIEU"
    
    def __str__(self):
        return f"{self.id} {self.name} {self.h} gio {self.m} phut {self.type}"    
n = int(input())
a = []

for _ in range(n):
    a.append(NV(input(), input(), input(), input()))
    
for nv in sorted(a, key=lambda x: (-x.time)):
    print(nv)