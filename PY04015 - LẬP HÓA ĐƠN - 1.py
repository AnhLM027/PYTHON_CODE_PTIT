
class KH:
    def __init__(self, id, name, csCu, csMoi):
        self.id = f"KH{id:02d}"
        self.name = name
        self.mk = csMoi - csCu
        if self.mk <= 50:
            self.tongTien = (self.mk * 100) * 1.02
        elif self.mk <= 100:
            self.tongTien = ((self.mk - 50) * 150 + 50  *100) * 1.03
        else:
            self.tongTien = ((self.mk - 100) * 200 + 50 * 100 + 50 * 150) * 1.05
            
n = int(input())
a = []
for i in range(1, n + 1):
    a.append(KH(i, input(), int(input()), int(input())))
    
for kh in sorted(a, key=lambda x: (-x.tongTien, x.id)):
    print(kh.id, kh.name, f'{kh.tongTien:.0f}')