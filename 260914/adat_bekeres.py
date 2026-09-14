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
össz1f = a+b
kül1f = a-b
print(f"A két szám összege: {össz1f}")
print(f"A két szám különbsége: {kül1f}")

# 2. feladat
valos = float(input("Kérlek adj meg egy valós számot: "))
valos10x = valos*10
print(f"A szám tízszeres: {valos10x}")

# 3. feladat
tavolsag = float(input("Kérlek add meg a megtett távolságot (km): "))
ido = float(input("Kérlek add meg az időt (óra): "))
atlagseb = tavolsag/ido
print(f"Az átlagsebesség: {atlagseb} km/h")

# 4. feladat
h_alap = abs(float(input("Kérlek add meg a háromszög alapját: ")))
h_magassag = abs(float(input("Kérlek add meg a magasságot: ")))
h_ter = h_alap*h_magassag/2
print(f"A háromszög területe: {h_ter} négyzetméter")

# 5. feladat
szam5f = int(input("Kérlek adj meg egy számot: "))
szam5f2x = szam5f*2
print(f"A szám kétszerese: {szam5f2x}")

# 6. feladat
szam6f = int(input("Kérlek adj meg egy tetszőleseges számot: "))
szam6fsqr = szam6f**2
szam6fcbr = szam6f**3
print(f"A szám négyzete: {szam6fsqr}, köbe: {szam6fcbr}")

# 7. feladat
cels = float(input("Kérlek adj meg egy Celsius fokot: "))
fahr = cels * 9/5 + 32
print(f"Ennyi celsius, {fahr} fahrenheit")

# 8. feladat
alap8f = float(input("Adj meg egy alapot: "))
kitevo8f = float(input("Adj meg egy kitevőt: "))
hatvany8f = alap8f ** kitevo8f
print(f"A hatvány {hatvany8f}")

# 9. feladat
szam9f = int(input("Adj meg egy számot: "))
szam29f = int(input("Adj meg egy második számot: "))
eredmeny9f = szam9f*2+szam29f/2
print(f"Eredmény: {eredmeny9f}")

# 10. feladat
km10f = abs(float(input("Adj meg egy számot (km): ")))
fogy10f = abs(float(input("Adj meg egy számot (liter/km): ")))
szüks10f = km10f * fogy10f
print(f"Szügséges üzemanyag: {szüks10f}")

# 11. feladat
oradij = abs(float(input("Add meg az óradíjad: ")))
munk_ora_szama = abs(int(input("Mennyi volt a munkaórák száma? ")))
fizetes = oradij * munk_ora_szama
print(f"Fizetés: {fizetes} Ft")

# 12. feladat
PI = 3.14
r = float(input("Add meg a kör sugarát: "))
k_ker = 2*r*PI
k_ter = r**2*PI

print(f"A kör kerülete: {k_ker}, területe: {k_ter}")

# 13. feladat
eletkor = abs(int(input("Adj meg egy életkort: "))) # nincs szükség rá a feladathoz
alv_szukseglet = abs(float(input("Add meg a napi alvásszükségletet: ")))
atl_alvas = alv_szukseglet*30
print(f"Átlagosan havi {atl_alvas} óra alvás szükséges")

# 14. feladat
atl_napi_lepes = abs(int(input("Add meg az átlagos napi lépésszámod: ")))
atl_napi_lepes_het_alatt = abs(int(input("Add meg az áltagos napi lépésszámod egy hét alatt: ")))
napi_atlag = (atl_napi_lepes + atl_napi_lepes_het_alatt) / 2
heti_atlag = napi_atlag * 7
print(f"A heti lépésátlag: {heti_atlag}")

# 15. feladat
nev15f = input("Add meg a nevet: ")
vagy = input("Mire gyűjt? ")
ar = int(input("Mennyibe kerül? "))
heti_zsp = abs(int(input("Heti zsebpénz: ")))
heti_kiad = abs(int(input("Heti kiadás: ")))
heti_net = heti_zsp - heti_kiad
hetek_szama = ar / heti_net
print(f"{hetek_szama} hét múlva tudja {nev15f} megvenni a {vagy}-t.")

# 16. feladat
magassag16f = abs(int(input("Milyen magas vagy? (cm-ben) ")))
magassag16fmeter = magassag16f/100
suly = abs(int(input("Hány kiló vagy? (kg) ")))
bmi = suly / magassag16fmeter ** 2
print(f"BMI: {bmi}")

# 17. feladat
alomsuly = int(input("Mi az álomsúlyod? "))
suly_kulonbseg = alomsuly-suly
for i in range(1, 4):
    heti_novekedes = suly_kulonbseg/3*i
    heti_cel = suly + heti_novekedes
    print(f"Az {i}. héten {heti_cel} kg-t kell elérned.")

# 18. feladat - sajnos nem java program
akt_ev = int(input("Mi az aktuális év? "))
szul_ev = int(input("Melyik évben született? "))
eletkor18f = akt_ev-szul_ev
szemkeret_ar = int(input("Mennyibe kerül a szemüvegkeret? "))
szemlencse_ar = int(input("Mennyibe kerül a szemüveg lencse ára? (1 pár lencse ára) "))
kedv_keret = ((100 - eletkor18f) / 100) * szemkeret_ar
kedv_ar = kedv_keret + szemlencse_ar
print(f"Ön a szemüvegkeret árából, ami {szemkeret_ar} Ft, {eletkor18f}% kedvezményt kap!\n" 
      f"A szemüveglencse ára: {szemlencse_ar} Ft\n"
      f"{'-'*20}\n" 
      f"Szemüveg vételára: {int(kedv_ar)}")