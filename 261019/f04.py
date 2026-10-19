import random
dobasokSzama = int(input("Dobasok szama: "))
osszPontszam = 0
hetesOsszegek = 0
legjobbDobas = 0
for i in range(dobasokSzama):
    print(f"{i+1}. dobas: ", end="")
    dobas1 = random.randint(1,6)
    dobas2 = random.randint(1,6)
    osszeg = dobas1 + dobas2
    print(f"{dobas1} + {dobas2} = {osszeg}", end="")
    if osszeg == 7:
        legjobbDobas = 10
        hetesOsszegek += 1
        osszPontszam += 10
        print(" -> 10 pont")
    elif dobas1 == dobas2:
        if legjobbDobas < 5:
            legjobbDobas = 5
        osszPontszam += 5
        print(f" -> 5 pont")
    else:
        if legjobbDobas < 1:
            legjobbDobas = 1
        osszPontszam += 1
        print(f" -> 1 pont")
print(f"Osszpontszam: {osszPontszam} Hetes osszegek: {hetesOsszegek} Legjobb dobas: {legjobbDobas} pont")