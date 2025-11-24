# Name,Age,Phone
# Alice,25,0912345678
# Bob,30,0923456789
# Charlie,22,0933456780


import csv

with open("contacts.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # đọc dòng đầu tiên là header
    print("Header:", header)
    
    for row in reader:
        name, age, phone = row[0], int(row[1]), row[2]
        print(f"{name} is {age} years old, phone: {phone}")

# Header: ['Name', 'Age', 'Phone']
# Alice is 25 years old, phone: 0912345678
# Bob is 30 years old, phone: 0923456789
# Charlie is 22 years old, phone: 0933456780

import csv

with open("contacts.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['Name']
        age = int(row['Age'])
        phone = row['Phone']
        print(f"{name} is {age} years old, phone: {phone}")

# Alice is 25 years old, phone: 0912345678
# Bob is 30 years old, phone: 0923456789
# Charlie is 22 years old, phone: 0933456780

