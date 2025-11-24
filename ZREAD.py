with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()       # đọc toàn bộ file thành 1 string

with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:           # duyệt từng dòng
        print(line.strip())  # strip() loại bỏ '\n'

with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()          # trả về list các dòng có '\n'
    lines = [line.strip() for line in lines]  # loại bỏ '\n'

with open("file.txt", "r", encoding="utf-8") as f:
    chunk = f.read(1024)   # đọc 1024 ký tự/lần



import csv

with open("file.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)  # trả về iterator
    data = [row for row in reader]  # list các hàng

with open("file.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # mỗi row là dict {header: value}
    for row in reader:
        print(row)

with open("file.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



import json

with open("file.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # trả về dict hoặc list

json_str = '{"Alice": "0912345678"}'
data = json.loads(json_str)  # parse string JSON thành dict



with open("file.bin", "rb") as f:
    content = f.read()  # đọc toàn bộ file nhị phân


import sys
line = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))



import sys
data = sys.stdin.read()  # đọc tất cả stdin
lines = data.splitlines()  # tách thành list các dòng



import sys
for line in sys.stdin:
    line = line.strip()
    print(line)
