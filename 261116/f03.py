import random

homersekletek = []

def feltoltes(db):
    for i in range(db):
        homersekletek.append(random.randint(0,100)*10)

def uj_homerseklet_rogzitese():
    ujHomerseklet = float(input("Új hőmérséklet: "))
    homersekletek.append(ujHomerseklet)
    print(f"{ujHomerseklet} adat rögzítésre került.")

def kiir():
    print("Hőmérsékletek: ")
    osszeg = 0
    for homerseklet in homersekletek:
        osszeg += homerseklet
        print(f"\t{homerseklet}")
    homersekletDb = len(homersekletek)
    if homersekletDb != 0:
        atlagHo = osszeg/len(homersekletek)
        print(f"Átlaghőmérséklet: {atlagHo}")
    else:
        print("A lista üres")

def kereses():
    keresettHo = float(input("Keresett hőmérséklet: "))
    if keresettHo in homersekletek:
        print(f"{keresettHo} szerepel a mérések között.")
    else:
        print(f"{keresettHo} nem szerepel a hőmérsékletek között.")

def rendrakas():
    homersekletek.sort()
    kiir()

def eltavolitas():
    eltavolitandoHo = float(input("Eltávolitandó hőmérséklet: "))
    if eltavolitandoHo in homersekletek:
        homersekletek.remove(eltavolitandoHo)
        print(f"{eltavolitandoHo} törölve a hőmérsékletek közül.")
    else:
        print("Ilyen mérési adat nem szerepel a rendszerben!")

def minden_kipakolasa():
    global homersekletek
    homersekletek = []

def main():
    feltoltes(10)
    kiir()
    uj_homerseklet_rogzitese()
    kiir()
    kereses()
    kiir()
    rendrakas()
    eltavolitas()
    kiir()
    minden_kipakolasa()
    kiir()

if __name__ == "__main__":
    main()
    