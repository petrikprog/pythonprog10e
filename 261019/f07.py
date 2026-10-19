import random
print("HUSZONEGY")
pont = 0
dobasokSzama = 0
felad = False
while True:
    szeretnelDobni = int(input("Szeretnel dobni? (1-igen, 0-nem): "))
    if szeretnelDobni == 0:
        felad = True
        break
    dobasokSzama += 1
    dobas1 = random.randint(1,6)
    dobas2 = random.randint(1,6)
    osszeg = dobas1 + dobas2
    pont += osszeg
    print(f"Dobas: {dobas1} + {dobas2} = {osszeg} Osszpontszam: {pont}")
    if pont > 21:
        print("Vesztettel! ", end="")
        break
    elif pont == 21:
        print("Nyertel! ", end="")
        break
if felad:
    print(f"Megalltal {pont} pontnal. {21-pont} ponttal maradtal el a 21-tol. ", end="")
print(f"Dobasok szama: {dobasokSzama}")
