import random
penz = 1000
nyeresekSzama = 0
while True:
    print(f"Egyenleg: {penz} Ft")
    tipp = int(input("Fej (1) vagy iras (2)? "))
    while True:
        tet = int(input("Tet: "))
        if tet > 0 and tet <= penz:
            break
        print("Helytelen tét")
    dobas = random.randint(1, 2)
    print(f"Dobas: {"fej" if dobas == 1 else "iras"}")
    if dobas == tipp:
        print(f"Nyertel {tet} Ft-ot!")
        penz += tet
        nyeresekSzama += 1
    else:
        print(f"Vesztettel {tet} Ft-ot!")
        penz -= tet
    if penz == 0:
        print("Vesztettel, elfogyott a penzed!")
        break
    folytatas = int(input("Folytatod? (1-igen, 0-nem): "))
    if folytatas == 0:
        break
print(f"Vegso egyenleg: {penz} Ft Megnyert korok: {nyeresekSzama}")