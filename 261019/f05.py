import random
porgetesekSzama = int(input("Porgetesek szama: "))
pont = 500
nullazasokSzama = 0
for i in range(porgetesekSzama):
    porgetes = random.randint(1, 10)
    print(f"{i+1}. porgetes: {porgetes} -> ", end="")
    if porgetes <= 3:
        pont += 100
        print("+100", end="")
    elif porgetes <= 6:
        pont += 200
        print("+200", end="")
    elif porgetes <= 8:
        pont -= 150
        print("-150", end="")
    elif porgetes == 9:
        pont *= 2
        print("duplazas", end="")
    else:
        pont = 0
        nullazasokSzama += 1
        print("nullazas", end="")
    print(f", egyenleg: {pont}")
print(f"Vegso pontszam: {pont} Nullazasok szama: {nullazasokSzama}")

