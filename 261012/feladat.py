import random

# 1. feladat
print("1f")
toke = abs(int(input("Kezdőtőke: ")))
kamat = abs(float(input("Kamat (%): ")))
kivantOsszeg = 300000
ev = 0
while toke < kivantOsszeg:
    toke += toke * (kamat/100)
    ev+=1
print(f"{ev} év alatt értük el a {kivantOsszeg} összeget.")

# 2. feladat
print("2f")
magassag = float(input("Magasság (m): "))
pattanas = 0
while magassag > 0.2:
    magassag *= 0.5
    pattanas+=1
print(pattanas)

# 3. feladat
print("3f")
szam3f = abs(int(input("Poz egész szám: ")))
muveletekSzama = 0
while szam3f != 1:
    print(szam3f)
    if szam3f % 2 == 0:
        szam3f /= 2
    else:
        szam3f *= 3
        szam3f += 1
    muveletekSzama += 1
print(f"{szam3f} lett a szám, {muveletekSzama} müvelet alatt.")  



# 4. feladat
print("4f")
felsoHatar = int(input("Felsőhatár: "))
hatvany = 0
while 2 ** (hatvany+1) < felsoHatar:
    hatvany += 1
print(f"A legnagyobb 2 hatvány a {felsoHatar} alatt a {2**hatvany}")


# 5. feladat
print("5f")
elerendoOsszeg = 500
osszeg = 0
i = 0
while True:
    szam5f = float(input("Adj meg egy számot: "))
    osszeg += szam5f
    i+=1
    if osszeg >= elerendoOsszeg:
        break
print(f"{osszeg} összeget értük el, {i} számból.")

# 6. feladat
print("6f")
jelszo = "titok123"
probalkozas = 0
while True:
    probaltJelszo = input("Add meg a jelszót: ")
    probalkozas += 1
    if probaltJelszo == jelszo:
        print("Sikeres belépés!")
        break
    print("Hibás jelszó, próbáld újra!")
print(f"A felhasználó sikeresen bejelentkezett {probalkozas} probalkozásból.")


# 7. feladat
print("7f")
while True:
    megadottSzo = input("Adj meg egy szót: ")
    if megadottSzo == "stopp" or megadottSzo == ".":
        print("Bye")
        break
    print(megadottSzo.upper())

    
# 8. feladat
print("8f")
while True:
    eletkor = int(input("Emberi életkor: "))
    if eletkor >= 0 and eletkor <= 120:
        print(f"Köszönöm, az életkorod: {eletkor}")
        break
    print("ERROR. Helytelen életkori érték.")

#############
# III. rész #
#############
resz3 = " III. rész "
resz3hastag =f"{"#"*(len(resz3)+2)}"
print(resz3hastag)
print(f"#{resz3}#")
print(resz3hastag)
# 1. feladat
print("1f")
while True:
    osszeg = abs(int(input("Összeghatár 1000 Ft alatt, osztható 5-tel: ")))
    if osszeg < 1000 and osszeg % 5 == 0:
        break
    print("ERROR. Helytelen érték.")

cimletek = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0}
while osszeg != 0:
    if osszeg >= 200:
        cimletek[200] += osszeg // 200
        osszeg %= 200
    if osszeg >= 100:
        cimletek[100] += osszeg // 100
        osszeg %= 100
    if osszeg >= 50:
        cimletek[50] += osszeg // 50
        osszeg %= 50
    if osszeg >= 20:
        cimletek[20] += osszeg // 20
        osszeg %= 20
    if osszeg >= 10:
        cimletek[10] += osszeg // 10
        osszeg %= 10
    if osszeg >= 5:
        cimletek[5] += osszeg // 5
        osszeg %= 5

print(f"{cimletek[200]} db 200as, {cimletek[100]} db 100as, {cimletek[50]} db 50es, {cimletek[20]} db 20as, {cimletek[10]} db 10es, {cimletek[5]} db 5ös")    


# 2. feladat
print("2f")
szam = int(input("Visszaszámlálás: "))
for i in range(szam, -1, -1):
    print(i)
print("Kilövés")


# 3. feladat
print("3f")
termekekSzama = 0
vegosszeg = 0
while True:
    ar = abs(int(input("Termék ára: ")))
    if ar == 0:
        break
    vegosszeg += ar
    termekekSzama += 1

print(f"{termekekSzama} terméket vásároltunk, {vegosszeg} Ft-ért")


# 4. feladat
print("4f")
bakteriumokSzama = 100
kivantBakterium = 50000
ora = 0
while bakteriumokSzama < kivantBakterium:
    bakteriumokSzama *=2
    ora += 1
print(f"{ora} óra alatt.")



# 5. feladat
print("5f")
szamsor = 1234
guessed = False
for i in range(3):
    tipp = int(input("Tippelj: "))
    if tipp == szamsor:
        guessed = True
        break
if guessed:
    print("Belépés engedélyezve!")
else:
    print("Letiltva!")



# 6. feladat
print("6f")
dobasokSzama = 0
while True:
    dobas = random.randint(1, 6)
    print(dobas)
    dobasokSzama += 1
    if dobas == 6:
        break
print(f"{dobasokSzama} dobásból sikerült 6ost dobnunk.")


# 7. feladat
print("7f")
while True:
    erdemjegy = int(input("Érdemjegy: "))
    if erdemjegy >= 1 and erdemjegy <= 5:
        print("Köszönöm, a jegyedet rögzítettem")
        break
    print("ERROR Hibás érték")

# 8. feladat
print("8f")
malacpersely = 0
nap = 0
while malacpersely <= 1000:
    felretettPenz = int(input("A mai nap félretett pénz: "))
    malacpersely += felretettPenz
    nap += 1
print(f"{nap} alatt érted el az 1000ft")



# 9. feladat
print("9f")
szam9f = 0
while szam9f < 1:
    szam9f = int(input("Egynél nagyobb egész szám: "))

oszto = 2
while szam9f % oszto != 0:
    oszto += 1

print(f"A legkisebb osztó: {oszto}")


# 10. feladat
print("10f")
while True:
    print("[1] Új Játék, [2] Segítség, [3] Kilépés")
    gomb = int(input("Gomb: "))
    if gomb == 1:
        print("Új Játék gomb megnyomva")
    elif gomb == 2:
        print("Segítség gomb megnyomva")
    elif gomb == 3:
        print("Kilépés folyamatban")
        break
    else:
        print("Nem létező gomb")
print("Kilépve")



