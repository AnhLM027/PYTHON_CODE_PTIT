import json

with open("flights.json", "r") as f:
    data = json.load(f)

data = data["flights"]

for i in range(int(input())):
    s = input().split()
    n = int(s[0])
    op = s[1]
    
    if op == "sum":
        res = 0
        for l in data:
            if int(l["year"]) == n: res += int(l["passengers"])
        print(res)
    if op == "min":
        res = 0
        for l in data:
            if int(l["year"]) == n: res = min(res, int(l["passengers"]))
        print(res)
    if op == "max":
        res = 0
        for l in data:
            if int(l["year"]) == n: res = max(res, int(l["passengers"]))
        print(res)
    if op == "avg":
        res = 0
        cnt = 0
        for l in data:
            if int(l["year"]) == n:
                res += int(l["passengers"])
                cnt += 1
        print(f"{(res / cnt):.5f}")