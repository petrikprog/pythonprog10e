import random
# 1. feladat
aktualisEmelet = random.randint(0,10)
celEmelet = random.randint(0,10)

emeletKulonbseg = aktualisEmelet - celEmelet
irany = ""
if emeletKulonbseg > 0:
    irany = "L"
elif emeletKulonbseg < 0:
    irany = "F"
else:
    irany = "-"

print(f"A lift helyzete: {aktualisEmelet} {irany} ({celEmelet})")

#2. feladat
hivoEmelet = int(input("Adje meg a szintet, ahonnan hívja a liftet! Szint: "))

#3. feladat
hivoKulonbseg = aktualisEmelet - hivoEmelet
if (hivoKulonbseg > 0 and emeletKulonbseg >= 0) or (hivoKulonbseg < 0 and emeletKulonbseg <= 0):
    print(f"A liftnek {abs(hivoKulonbseg)} emeletet kell haladnia a hívóig.")
else:
    celHivoTavolsag = abs(celEmelet - hivoEmelet)
    teljesTavolsag = abs(emeletKulonbseg) + celHivoTavolsag
    print(f"A liftnek {teljesTavolsag} emeletet kell haladnia a hívóig.")
