import json
import pandas as pd

# Đọc file JSON
with open("File.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Làm phẳng dữ liệu (nếu JSON lồng nhau)
df = pd.json_normalize(data, record_path=["cameras"], sep=".")

# Xuất ra CSV
df.to_csv("output.csv", index=False, encoding="utf-8-sig")
