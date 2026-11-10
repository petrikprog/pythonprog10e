#1. feladat
meresiAdatok = [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]

print("2. feladat")
osszesKerekparos = 0
for adat in meresiAdatok:
    if adat != -1:
        osszesKerekparos += adat
print(f"Összesen {osszesKerekparos} kerékpárost számoltak.")

print("3. feladat")
print("Óránkénti mérések")
jelenlegiOra = 6
osszKerekparosPerOra = 0
for i in range(len(meresiAdatok)):
    adat = meresiAdatok[i]
    osszKerekparosPerOra += adat
    if i % 4 == 2:
        print(f"{jelenlegiOra} órától {osszKerekparosPerOra} kerékpáros")
        osszKerekparosPerOra = 0
        jelenlegiOra += 1

print("4. feladat")
maxErtek = -1
maxErtekIdopontja = "0:00"
for i in range(len(meresiAdatok)):
    adat = meresiAdatok[i]
    if adat > maxErtek:
        maxErtek = adat
        ora = (i+1) // 4 + 6
        perc = ((i+1) % 4) * 15
        if perc == 0:
            maxErtekIdopontja = f"{ora}:{perc}0"
        else:
            maxErtekIdopontja = f"{ora}:{perc}"
            
        
print(f"Az áthaladók maximális száma: {maxErtek}; a rögzités időpontja {maxErtekIdopontja}")