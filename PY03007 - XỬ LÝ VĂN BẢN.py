import sys, re

s = sys.stdin.read()
s = re.sub(r'\s+', ' ', s.strip())
sentences = re.split(r'[.!?]+', s)

for sen in sentences:
    sen = sen.strip()
    if sen == "":
        continue
    sen = re.sub(r'\s+', ' ', sen.lower())
    sen = sen[0].upper() + sen[1:]
    print(sen)
