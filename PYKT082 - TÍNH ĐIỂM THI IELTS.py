
def band_score(n):
    if n >= 39: return 9.0
    elif n >= 37: return 8.5
    elif n >= 35: return 8.0
    elif n >= 33: return 7.5
    elif n >= 30: return 7.0
    elif n >= 27: return 6.5
    elif n >= 23: return 6.0
    elif n >= 20: return 5.5
    elif n >= 16: return 5.0
    elif n >= 13: return 4.5
    elif n >= 10: return 4.0
    elif n >= 7: return 3.5
    elif n >= 5: return 3.0
    elif n >= 3: return 2.5
    else: return 1.0

def cv(score):
    tmp = score - int(score)
    if abs(tmp - 0.25) < 1e-6: return int(score) + 0.5
    elif abs(tmp - 0.75) < 1e-6: return int(score) + 1.0
    else: return round(score * 2) / 2

T = int(input())
for _ in range(T):
    r, l, s, w = input().split()
    r = int(r)
    l = int(l)
    s = float(s)
    w = float(w)
    read_score = band_score(r)
    listen_score = band_score(l)
    overall = (read_score + listen_score + s + w) / 4
    overall = cv(overall)
    print(f"{overall:.1f}")
