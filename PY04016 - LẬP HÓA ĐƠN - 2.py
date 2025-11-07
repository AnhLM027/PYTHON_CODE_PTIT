
from datetime import datetime

class KH:
    def __init__(self, id, name, room, start, end, extra):
        self.id = f"KH{id:02d}"
        self.name = name.strip()
        self.room = room.strip()
        self.extra = int(extra)
        self.days = (datetime.strptime(end, "%d/%m/%Y") - datetime.strptime(start, "%d/%m/%Y")).days + 1
        
        floor = int(room[0])
        price = {1: 25, 2: 34, 3: 50, 4: 80}.get(floor, 25) 
        self.total = self.days * price + self.extra

    def __str__(self):
        return f"{self.id} {self.name} {self.room} {self.days} {self.total}"

n = int(input())
a = []
for i in range(1, n + 1):
    a.append(KH(i, input(), input(), input().strip(), input().strip(), input()))

for kh in sorted(a, key=lambda x: -x.total):
    print(kh)
