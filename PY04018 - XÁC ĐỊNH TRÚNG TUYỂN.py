
class GV:
    def __init__(self, id, name, ma, d1, d2):
        self.id = f"GV{id:02d}"
        self.name = name
        
        hash = {1: 2.0, 2: 1.5, 3: 1.0, 4: 0}
        type, dut = ma[0], float(hash.get(int(ma[1])))
        if type == 'A':
            self.mon = 'TOAN'
        elif type == 'B':
            self.mon = 'LY'
        else: self.mon = 'HOA'
        self.tongDiem = d1 * 2 + d2 + dut
        self.xl = "TRUNG TUYEN" if self.tongDiem >= 18 else "LOAI"

    def __str__(self):
        return f"{self.id} {self.name} {self.mon} {self.tongDiem:.1f} {self.xl}"

n = int(input())
a = []
for i in range(1, n + 1):
    a.append(GV(i, input(), input(), float(input()), float(input())))

for gv in sorted(a, key=lambda x: -x.tongDiem):
    print(gv)
