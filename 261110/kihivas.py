print("1. feladat")
hetiAktivitas = input("Adja meg a heti aktivitását: ").upper()

print("2. feladat")
karakterTavolsag = {'U': 1, 'G': 1, 'F': 2, 'K': 10}
karakterTevekenyseg = {'U': "Úszás", 'G': "Gyaloglás", 'F': "Futás", 'K': "Kerékpározás"}
tevekenysegVolt = {"Úszás": False, "Gyaloglás": False, "Futás": False, "Kerékpározás": False}
hetiKm = 0
utolsoKarakter = ''
utolsoKarakterIsmetlesenekSzama = 0

def ReturnAndCalculateTevekenysegString(utolsoKarakter, utolsoKarakterIsmetlesenekSzama):
    global hetiKm
    tevekenyseg = karakterTevekenyseg[utolsoKarakter]
    tevekenysegErteke = karakterTavolsag[utolsoKarakter]
    megtettTav = tevekenysegErteke*utolsoKarakterIsmetlesenekSzama
    hetiKm += megtettTav
    tevekenysegVolt[tevekenyseg] = True
    return f"{utolsoKarakter*utolsoKarakterIsmetlesenekSzama} - {megtettTav} km {tevekenyseg}"


for karakter in hetiAktivitas:
    if not utolsoKarakter:
        utolsoKarakter = karakter
        utolsoKarakterIsmetlesenekSzama = 1
    if karakter == utolsoKarakter:
        utolsoKarakterIsmetlesenekSzama += 1
    else:
        print(f"{ReturnAndCalculateTevekenysegString(utolsoKarakter, utolsoKarakterIsmetlesenekSzama)}, ", end="")
        utolsoKarakter = karakter
        utolsoKarakterIsmetlesenekSzama = 1

print(f"{ReturnAndCalculateTevekenysegString(utolsoKarakter, utolsoKarakterIsmetlesenekSzama)}. ", end="")


print(f"Ezzel {hetiKm} kilométert teljesített.")

print("3. feladat")
mindenFeladatVolt = True
for feladatVolt in tevekenysegVolt.values():
    if not feladatVolt:
        mindenFeladatVolt = False
        break
if mindenFeladatVolt:
    hetiKm += 10
    print("Bravó! Jutalma még 10 km.")

print("4. feladat")
print(f"A héten gyűtött kilométerek száma: {hetiKm}")
if hetiKm >= 40:
    print("Gratulálok, kihívás teljesítve!")
else:
    print("Legközelebb sikerül!")
