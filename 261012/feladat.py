"""
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
"""
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
    osszegHatar = abs(int(input("Összeghatár 1000 Ft alatt, osztható 5-tel: ")))
    if osszegHatar < 1000 and osszegHatar % 5 == 0:
        break
    print("ERROR. Helytelen érték.")


