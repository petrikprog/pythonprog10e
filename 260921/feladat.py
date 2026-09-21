# 1. Feladat
egyikSzam = int(input("Adj meg egy számot: "))
masikSzam = int(input("Adj meg egy másik számot: "))

b = egyikSzam > 0 and masikSzam > 0
print(b)

igazE = egyikSzam < 4 and masikSzam != 6
print(igazE)

if egyikSzam == 0 or masikSzam == 0:
    print("Van 0")

if egyikSzam == 5 or masikSzam != 4:
    print("Vagy 5 vagy nem 4")

if egyikSzam <= 5 or masikSzam > 13:
    print("kisebb 5 v nagyobb 13")

if egyikSzam > 0 and masikSzam < 0:
    print("poz és neg")

# 2. Feladat
zold = '\033[92m'
alap = '\033[0m'
print(f"{alap}\tNegáció\nA\t\t{zold}not A{alap}\nI\t\t{zold}H\n{alap}H\t\t{zold}I")
print(f"{alap}\tVagy\nA\tB\t{zold}A or B{alap}\nH\tH\t{zold}H\n{alap}I\tH\t{zold}I\n{alap}H\tI\t{zold}I\n{alap}I\tI\t{zold}I")
print(f"{alap}\tÉs\nA\tB\t{zold}A and B\n{alap}H\tH\t{zold}H\n{alap}I\tH\t{zold}H\n{alap}H\tI\t{zold}H\n{alap}I\tI\t{zold}I")
print(f"{alap}\tKizáró vagy\nH\tH\t{zold}H\n{alap}I\tH\t{zold}I\n{alap}H\tI\t{zold}I\n{alap}I\tI\t{zold}H{alap}")

# 3. Feladat
szam3f = int(input("Adj meg egy számot: "))
maradek3f = szam3f % 10
if maradek3f != 0:
    print(maradek3f)
else:
    print("A szám osztható 10-zel.")

# 4. feladat
szamlalo = int(input("Számláló: "))
nevezo = int(input("Nevező: "))
try:
    f4=szamlalo/nevezo
except ZeroDivisionError:
    print("Nem lehet 0-val osztani")

# 5. feladat
szam5fstr = input("3 jegyű poz. egész szám: ")
szam5f = abs(int(szam5fstr))
szum = 0
for i in range(0, len(szam5fstr)):
    num = int(szam5fstr[i])
    szum += num ** 3

if szum == szam5f:
    print("Armstrong szám")
else:
    print("Nem Armstrong szám")

# 6. feladat
szam6f = int(input("Szám6f: "))
if szam6f == 4:
    print("A megadott szám a 4-es.")

if szam6f < 10:
    print("A megadott szám kisebb mint 10.")

if szam6f % 2 == 0:
    print("A megadott szám páros.")

if szam6f in range(0,11):
    print("A megadott szám a [0,10] intervallumba esik.")

if szam6f % 3 == 0 and szam6f % 5 == 0:
    print("A megadott szám osztható 3-mal és 5-tel is.")

if szam6f not in range(10,21):
    print("A megadott szám nem a [10,20] intervallumba esik.")

# 7. feladat
szam7f1 = int(input("Szám 1: "))
szam7f2 = int(input("Szám 2: "))

if szam7f1 == szam7f2:
    print("A két szám egyenlő.")

if szam7f1 % 2 == 1 and szam7f2 % 2 == 1:
    print("Mind a két szám páratlan.")

if szam7f1 % 3 == 0 or szam7f2 % 3 == 0:
    print("Legalább az egyik szám osztható hárommal.")

if szam7f1 < 0 and szam7f2 < 0:
    print("Mind a két szám negatív.")

if (szam7f1 < 0 and szam7f2 > 0) or (szam7f1 > 0 and szam7f2 < 0):
    print("Az egyik szám negatív, a másik szám pozitív.")

# 8. feladat
szam8fa = float(input("A téglalap a oldala: "))
szam8fb = float(input("A téglalap b oldala: "))
if szam8fa == szam8fb:
    print("A szám négyzet")
else:
    print("A a szám téglalap")

# 9. feladat
szam9fa = float(input("A hszög a oldala: "))
szam9fb = float(input("A hszög b oldala: "))
szam9fc = float(input("A hszög c oldala: "))

if szam9fa == szam8fb == szam9fc:
    print("Szabályos háromszög")
else:
    print("Nem szabályos háromszög")

# 10. feladat
szam10f = int(input("Egész szám: "))
if szam10f == 10:
    print("A szám 10")
elif szam10f == 100:
    print("A szám 100")
elif szam10f == 1000:
    print("A szám 1000")

# 11. feladat
szam11f = int(input("Szám: "))
if szam11f in range(1,10):
    print("A szám benne van a 1,9 intervallumban.")

# 12. feladat
szam12f = int(input("Szám: "))
if szam12f < 0 and szam12f % 2 == 0:
    print("negatív páratlan")

# 13. feladat
szam13f1 = int(input("Szám 1: "))
szam13f2 = int(input("Szám 2: "))
if szam13f2 % szam13f1 == 0:
    print("A szám osztója a másiknak")