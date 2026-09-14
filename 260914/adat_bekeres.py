nev = input("Kérem adja meg a nevét: ")
print(f"Üdvözöllek {nev}")

ev = int(input("Kérem adja meg a születési évét: "))

kor = 2026 - ev
print(f"Az életkorod kedves {nev}: {kor}")

magassag = float(input("Kérem adja meg a magasságát: "))
print(f"A magasságod kedved {nev}: {magassag}")

# 1. feladat
a = int(input("Kérlek add meg az első számot: "))
b = int(input("Kérlek add meg a második számot: "))
print(f"A két szám összege: {a+b}")
print(f"A két szám különbsége: {a-b}")

# 2. feladat
valos = float(input("Kérlek adj meg egy valós számot: "))
print(f"A szám tízszeres: {valos*10}")

# 3. feladat
tavolsag = float(input("Kérlek add meg a megtett távolságot (km): "))
ido = float(input("Kérlek add meg az időt (óra): "))
print(f"Az átlagsebesség: {tavolsag/ido}")

# 4. feladat
h_alap = float(input("Kérlek add meg a háromszög alapját: "))
h_magassag = float(input("Kérlek add meg a magasságot: "))
print(f"A háromszög területe: {h_alap*h_magassag/2} négyzetméter")

# 5. feladat
tetszszam = float(input("Kérlek adj meg egy számot: "))
print(f"A szám kétszerese: {tetszszam*2}")

# 6. feladat
szam6f = float(input("Kérlek adj meg egy tetszőleseges számot: "))
print(f"A szám négyzete: {szam6f**2}, köbe: {szam6f**3}")

# 7. feladat
cels = float(input("Kérlek adj meg egy Celsius fokot: "))
print(f"Ennyi celsius, {cels * 9/5 + 32} fahrenheit")

# 8. feladat
alap8f = float(input("Adj meg egy alapot: "))
kitevo8f = float(input("Adj meg egy kitevőt: "))
print(f"A hatvány {alap8f**kitevo8f}")

# 9. feladat
szam9f = float(input("Adj meg egy számot:: "))
szam29f = float(input("Adj meg egy második számot: "))
print(f"Eredmény: {szam9f*2+szam29f/2}")

# 10. feladat
km10f = float(input("Adj meg egy számot (km): "))
fogy10f = float(input("Adj meg egy számot (liter/km): "))
print(f"Szügséges üzemanyag: {km10f*fogy10f}")
