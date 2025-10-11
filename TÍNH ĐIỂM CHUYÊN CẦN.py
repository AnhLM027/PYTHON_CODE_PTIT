

class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem_danh = ""
        self.diem_cc = 10

    def set_diem_danh(self, tt):
        self.diem_danh = tt
        self.tinh_diem_cc()

    def tinh_diem_cc(self):
        diem = 10
        for c in self.diem_danh:
            if c == 'm': diem -= 1
            elif c == 'v': diem -= 2
            
        self.diem_cc = max(0, diem)

    def __str__(self):
        if self.diem_cc == 0: return f"{self.ma} {self.ten} {self.lop} {self.diem_cc} KDDK"
        else:
            return f"{self.ma} {self.ten} {self.lop} {self.diem_cc}"
        
n = int(input())
res = []

for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    sv = SinhVien(ma, ten, lop)
    res.append(sv)
    
for _ in range(n):
    line = input().strip().split()
    ma_sv = line[0]
    diem_danh = line[1]
    for sv in res:
        if sv.ma == ma_sv:
            sv.set_diem_danh(diem_danh)
            break

for sv in res:
    print(sv)