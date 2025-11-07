import math

with open("DATA.in", "r") as f:
    words = []
    for line in f:
        for w in line.split():
            try:
                int(w)
                if int(w) > (2 ** 32):
                    words.append(w)
            except ValueError:
                words.append(w)
                
words.sort()
print(' '.join(words))
