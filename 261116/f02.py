import random
pontszamok = []

def feltoltes(db):
    for i in range(db):
        pontszamok.append(random.randint(0,100)*10)

def uj_pontszam_rogzitese():
    ujPontszam = int(input("Új elért pontszám: "))
    pontszamok.append(ujPontszam)
    print(f"A(z) {ujPontszam} pont bekerült a toplistára!")

def kiir():
    print("Toplista: ")
    for pont in pontszamok:
        print(f"\t{pont}")
    print(f"Eddig {len(pontszamok)} pont van a listában.")

def kereses():
    keresettPontszam = int(input("Keresett pontszám: "))
    if keresettPontszam in pontszamok:
        print("Szerepel a rekordok között.")
    else:
        print("Nem szerepel a rekordok között.")

def rendrakas():
    pontszamok.sort(reverse=True)
    kiir()

def eltavolitas():
    eltavolitandoPontsztam = int(input("Melyik pontszámot szeretnéd törölni? "))
    if eltavolitandoPontsztam in pontszamok:
        pontszamok.remove(eltavolitandoPontsztam)
        print("Törölve.")
    else:
        print("Ezt a pontszámot még senki sem érte el ebben a formában!")

def minden_kipakolasa():
    global pontszamok
    pontszamok = []

def main():
    feltoltes(10)
    uj_pontszam_rogzitese()
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