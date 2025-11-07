
with open('VANBAN.in', 'r', encoding='utf-8') as f:
    words = f.read().split()

lower_words = [w for w in words]

palindromes = [w for w in lower_words if w == w[::-1]]

if palindromes:
    max_len = max(len(w) for w in palindromes)
    freq = {}
    order = []
    for w in lower_words:
        if w == w[::-1] and len(w) == max_len:
            if w not in freq:
                freq[w] = lower_words.count(w)
                order.append(w)

    for w in order:
        print(w, freq[w])
