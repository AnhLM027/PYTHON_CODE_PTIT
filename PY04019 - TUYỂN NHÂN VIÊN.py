import math

class SV:
    def __init__(self, id, name, d1, d2):
        self.id = f'TS0{str(id)}'
        self.name = name
        self.dtb = ((d1 if d1 <= 10 else d1 / 10) + (d2 if d2 <= 10 else d2 / 10)) / 2
        
        if self.dtb < 5: self.type = "TRUOT"
        elif self.dtb < 8: self.type = "CAN NHAC"
        elif self.dtb <= 9.5: self.type = "DAT"
        else: self.type = "XUAT SAC"
        
a = []
for i in range(int(input())):
    a.append(SV(i + 1, input(), float(input()), float(input())))
    
for sv in sorted(a, key = lambda x: (-x.dtb, x.id)):
    print(sv.id, sv.name, f"{sv.dtb:.2f}", sv.type)