import csv

with open("penguins.csv", "r") as f:
    data = csv.DictReader(f)
        
    for _ in range(int(input())):
        loai, dao = input().split()
        cnt1, cnt2, avg_len, avg_depth = 0, 0, 0, 0
        for l in data:
            if l["species"] == loai and l["island"] == dao:
                try:
                    cnt1 += 1
                    avg_len += float(l["bill_length_mm"])
                except: pass
                try:
                    cnt2 += 1
                    avg_depth += float(l["bill_depth_mm"])
                except: pass
        print(f"{(avg_len / cnt1):.4f} {(avg_depth / cnt2): }")