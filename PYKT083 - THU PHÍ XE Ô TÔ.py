
mp = {}

pt = {"Xe_con 5": 10000,
      "Xe_con 7": 15000,
      "Xe_tai 2": 20000,
      "Xe_khach 29": 50000,
      "Xe_khach 45": 70000,
    }

for _ in range(int(input())):
    arr = input().split()
    if arr[3] == "OUT": continue
    
    time = arr[-1]
    mp[arr[-1]] = mp.get(arr[-1], 0) + pt[arr[1] + " " + arr[2]]
    
res = list(mp.items())
for v in sorted(res, key=lambda x: x[0]):
    print(f"{v[0]}: {v[1]}")