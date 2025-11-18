from datetime import datetime

class CaThi:
    def __init__(self, id, date, time, room):
        self.id = f"C{id:03d}"
        self.date = date
        self.time = time
        self.room = room
        self.datetime = datetime.strptime(f"{date} {time}", "%d/%m/%Y %H:%M")

    def __str__(self):
        return f"{self.id} {self.date} {self.time} {self.room}"

with open("CATHI.in") as f:
    data = f.read().strip().splitlines()

n = int(data[0])
a = []
idx = 1
for i in range(1, n + 1):
    date = data[idx].strip()
    time = data[idx + 1].strip()
    room = data[idx + 2].strip()
    a.append(CaThi(i, date, time, room))
    idx += 3

a.sort(key=lambda x: (x.datetime, x.id))

for ct in a:
    print(ct)
