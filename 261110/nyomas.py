#1. feladat
meresiAdatok = [865, 846, 831, 820, 808, 783, 788, 775, 752, 750, 743, 745, 758, 770]

#2. feladat
minAdat = 10**10
minAdatIndex = -1

for i in range(len(meresiAdatok)):
    adat = meresiAdatok[i]
    if adat < minAdat:
        minAdat = adat
        minAdatIndex = i

print(f"A legkisebb mért érték: {minAdat}")
print(f"Legkisebb mérési adat sorszáma: {minAdatIndex+1}")

#3. feladat
hatarertek = int(input("Minél kisebb értéket keres? (egész szám) "))
hatarertekAlattiSzam = 0
for adat in meresiAdatok:
    if adat < hatarertek:
        hatarertekAlattiSzam += 1
print(f"{hatarertek} alatti mérések száma: {hatarertekAlattiSzam}")

#4. feladat
maxCsokkenes = -1
elozoSzam = -1
for adat in meresiAdatok:
    if elozoSzam != -1:
        csokkenes = elozoSzam-adat
        if csokkenes > maxCsokkenes:
            maxCsokkenes = csokkenes
    elozoSzam = adat
print(f"A két mérés közötti legnagyobb csökkenés: {maxCsokkenes}")