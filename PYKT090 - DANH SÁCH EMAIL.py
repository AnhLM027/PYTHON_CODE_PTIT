
with open('CONTACT.in', 'r', encoding='utf-8') as f:
    emails = f.read().split()

emails = [e.lower() for e in emails]
res = sorted(set(emails))

for e in res:
    print(e)
