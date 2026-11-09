import random
tippek = []

for i in range(5):
    while 1:
        tipp = int(input("Szám 1-90 között, ami még nem szerepel az eddigi számok között: "))
        if tipp >= 1 and tipp <= 90 and tipp not in tippek:
            tippek.append(tipp)
            break
        print("HELYTELEN ÉRTÉK")

nyeroszamok = []
for i in range(5):
    while 1:
        nyeroszam = random.randint(1,90)
        if nyeroszam not in nyeroszamok:
            nyeroszamok.append(nyeroszam)
            break
talalatokSzama = 0

for tipp in tippek:
    if tipp in nyeroszamok:
        talalatokSzama += 1

print(nyeroszamok)
print(f"{talalatokSzama} találatod volt!")
