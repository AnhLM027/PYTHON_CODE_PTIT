
with open("DATA1.in") as f1:
    s1 = set(f1.read().lower().split())

with open("DATA2.in") as f2:
    s2 = set(f2.read().lower().split())
    
print(" ".join(sorted(s1 - s2)))
print(" ".join(sorted(s2 - s1)))