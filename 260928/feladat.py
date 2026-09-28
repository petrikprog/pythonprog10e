import random as rand
import math

# 21. feladat
print("21f")
pontszam = int(input("Pontszám: "))

if pontszam <= 42:
    print("Elégtelen")
elif pontszam <= 57:
    print("Elégséges")
elif pontszam <= 72:
    print("Közepes")
elif pontszam <= 87:
    print("Jó")
else:
    print("Jeles")

# 22. feladat
print("22f")
eletkor = abs(int(input("Életkor: ")))

if eletkor <= 13:
    print("Gyerek")
elif eletkor <= 17:
    print("Fiatalkorú")
elif eletkor <= 23:
    print("Ifjú")
elif eletkor <= 59:
    print("Felnőtt")
else:
    print("Idős")

# 23. feladat
print("23f")

targySuruseg = float(input("Sűrűség tárgy: "))
folyadekSuruseg = float(input("Folyadék sűrűség: "))

if targySuruseg > folyadekSuruseg:
    print("Elmerűl")
elif folyadekSuruseg > targySuruseg:
    print("Úszik")
else:
    print("Lebeg")

# 24. feladat
print("24f")

igazolatlan = int(input("Hiányzás száma: "))
if igazolatlan == 0:
    print("5")
elif igazolatlan <= 3:
    print("4")
elif igazolatlan <= 9:
    print("3")
elif igazolatlan >= 10:
    print("2")
    szuletesiEv = int(input("Születési év: "))
    eletkor24f = 2026 - szuletesiEv

    if eletkor24f < 18:
        print("szülői értesítés szükséges")
    else:
        print("felszólítás kiküldése szükséges")

# 25. feladat
print("25f")

karakter = input("Karakter: ")
ascii25f = ord(karakter)

if ascii25f >= 48 and ascii25f <= 57:
    print("Számok")
elif ascii25f >= 65 and ascii25f <= 90:
    print("Nagy angol ABC betűi")
elif ascii25f >= 97 and ascii25f <= 122:
    print("Kis angol ABC betűi")

# 26. feladat
print("26f")

sebesseg = int(input("Sebesség: "))

if sebesseg <= 1:
    print("csiga")
elif sebesseg <= 6:
    print("csuka")
elif sebesseg <= 32:
    print("bálna")
elif sebesseg <= 48:
    print("ezüst sirály")
elif sebesseg <= 64:
    print("nyúl")
elif sebesseg <= 70:
    print("strucc")
elif sebesseg <= 110:
    print("gepárd")
elif sebesseg <= 320:
    print("vadászsólyom(zuhanórepülésben)")

# 27. feladat
print("27f")

tavolsag = int(input("Távolság: "))

if tavolsag >= 1 and tavolsag <= 2:
    print("500ft")
elif tavolsag <= 5:
    print("700ft")
elif tavolsag <= 10:
    print("900ft")
elif tavolsag <= 20:
    print("1400ft")
elif tavolsag <= 30:
    print("2000ft")

# 28 .feladat
print("28f")

szelesseg = float(input("Szélesség: "))
hosszusag = float(input("Hosszúság: "))
telekAdo = float(input("Helyi telek adó: "))

if szelesseg <= 15 and hosszusag <= 25:
    telekAdo *= 0.8
    print(telekAdo)

# 29. feladat
print("29f")

t = int(input("Évszám: "))

a = t % 19
b = t % 4
c = t % 7
d = (19*a + 24) % 30
e = (2*b+4*c+6*d+5) % 7
h = 22 + d + e

if e == 6 and d == 29:
    h = 50
elif e == 6 and d == 28 and a > 10:
    h = 49

if h <= 31:
    print(f"március {h}")
else:
    print(f"április {h-31}")

# 30. feladat
print("30f")

erdemjegy = int(input("Érdemjegy: "))

if erdemjegy == 5:
    print("jeles")
elif erdemjegy == 4:
    print("jó")
elif erdemjegy == 3:
    print("közepes")
elif erdemjegy == 2:
    print("elégsegés")
elif erdemjegy == 1:
    print("elégtelen")

# 31. feladat
print("31f")

het = int(input("A hét napja (szám): "))

if het == 1:
    print("Hétfő")
elif het == 2:
    print("Kedd")
elif het == 3:
    print("Szerda")
elif het == 4:
    print("Csütörtök")
elif het == 5:
    print("Péntek")
elif het == 6:
    print("Szombat")
elif het == 7:
    print("Vasárnap")

# 32. feladat
print("32f")

ev = int(input("Év: "))
honap = int(input("Hónap (szám): "))
nap = int(input("Nap: "))

if honap == 1:
    honap = "Január"
elif honap == 2:
    honap = "Február"
elif honap == 3:
    honap = "Március"
elif honap == 4:
    honap = "Április"
elif honap == 5:
    honap = "Május"
elif honap == 6:
    honap = "Június"
elif honap == 7:
    honap = "Július"
elif honap == 8:
    honap = "Augusztus"
elif honap == 9:
    honap = "Szeptember"
elif honap == 10:
    honap = "Október"
elif honap == 11:
    honap = "November"
elif honap == 12:
    honap = "December"

print(f"{ev}. {honap} {nap}.")

# 33. feladat
print("33f")

dobas = int(input("Dobás: "))
if dobas <= 2:
    print("Gyenge!")
elif dobas <= 4:
    print("Nem rossz!")
elif dobas == 5:
    print("Jó!")
else:
    print("Kiváló!")

# 34. feladat
print("34f")
print(rand.randint(0,100))
print(rand.randint(-100,0))
print(rand.randint(10,90))
print(rand.randint(-100,100))
print(rand.randint(-50,50))
print(rand.randint(1000,2000))
print(rand.randint(8000,150000))

# 35. feladat
print("35f")
lab = float(input("Láb: "))
huvelyk = float(input("Hüvelyk: "))

print(f"Láb {lab * 30.48} cm, hüvelyk {huvelyk * 2.54} cm")