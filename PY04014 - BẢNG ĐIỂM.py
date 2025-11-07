from functools import reduce
import math

class SV:
    def __init__(self, name, arr, cnt):
        self.name = name
        self.msv = f"HS{cnt:02d}"
        self.tb = (arr[0]*2 + arr[1]*2 + reduce(lambda x, y: x+y, arr[2:])) / 12
        self.tb = math.floor(self.tb * 10 + 0.5) / 10
        
    def danhgia(self):
        if self.tb < 5: return "YEU"
        elif self.tb < 7: return "TB"
        elif self.tb < 8: return "KHA"
        elif self.tb < 9: return "GIOI"
        return "XUAT SAC"


n = int(input())

a = []
for i in range(1, n + 1):
    name = input().strip()
    arr = list(map(float, input().split()))
    a.append(SV(name, arr, i))

for sv in sorted(a, key=lambda x: (-x.tb, x.msv)):
    print(f"{sv.msv} {sv.name} {sv.tb:.1f} {sv.danhgia()}")