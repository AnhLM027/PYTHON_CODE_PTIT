
def chd(a, b):
    if b == 1: return "Ma Ket" if a <= 19 else "Bao Binh"
    elif b == 2: return "Bao Binh" if a <= 18 else "Song Ngu"
    elif b == 3: return "Song Ngu" if a <= 20 else "Bach Duong"
    elif b == 4: return "Bach Duong" if a <= 19 else "Kim Nguu"
    elif b == 5: return "Kim Nguu" if a <= 20 else "Song Tu"
    elif b == 6: return "Song Tu" if a <= 20 else "Cu Giai"
    elif b == 7: return "Cu Giai" if a <= 22 else "Su Tu"
    elif b == 8: return "Su Tu" if a <= 22 else "Xu Nu"
    elif b == 9: return "Xu Nu" if a <= 22 else "Thien Binh"
    elif b == 10: return "Thien Binh" if a <= 22 else "Thien Yet"
    elif b == 11: return "Thien Yet" if a <= 22 else "Nhan Ma"
    elif b == 12: return "Nhan Ma" if a <= 21 else "Ma Ket"

def main():
    a, b = map(int, input().split())
    print(chd(a, b))

for tc in range(int(input())):
    main()