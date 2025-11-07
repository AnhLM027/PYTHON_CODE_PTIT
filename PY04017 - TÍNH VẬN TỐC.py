import math

class TS:
    def __init__(self, ma, name, address, time):
        self.ma = ma
        self.name = name
        self.address = address
        h, m = map(int, time.split(":"))
        self.time = ((h - 6) * 60 + m) / 60
        self.vt = round(120 / self.time)

    def __str__(self):
        return f"{self.ma} {self.name} {self.address} {self.vt} Km/h"

n = int(input())
a = []
for i in range(1, n + 1):
    name = input()
    address = input()
    time = input()
    tkName = name.split(" ")
    tkAd = address.split(" ")
    ma = ""
    for w in tkAd: ma += w[0].upper()
    for w in tkName: ma += w[0].upper()
    a.append(TS(ma, name, address, time))

for ts in sorted(a, key=lambda x: x.time):
    print(ts)
