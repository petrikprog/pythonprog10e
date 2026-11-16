hatizsak = ["kard", "gyógyital", "térkép", "fáklya"]

def hatizsak_feltoltes():
    ujTargy = input("Milyen tárgyat találtál a barlangban? ")
    hatizsak.append(ujTargy)
    print(f"{ujTargy} hátizsákba berakva.")

def kiir():
    print("Hátizsák tartalma:")
    for targy in hatizsak:
        print(f"\t{targy}")
    print(f"Jelenleg {len(hatizsak)} tárgy van a táskában.")

def kereses():
    keresettTargy = input("Melyik tárgyat keresed? ")
    if keresettTargy in hatizsak:
        print(f"Benne van a táskában a(z) {hatizsak.index(keresettTargy)+1}. helyen.")
    else:
        print(f"Nincs ilyen tárgy a táskában.")

def rendrakas():
    hatizsak.sort()

def eltavolitas():
    eltavolitandoTargy = input("Melyik tárgyat szeretnéd törölni? ")
    if eltavolitandoTargy in hatizsak:
        hatizsak.remove(eltavolitandoTargy)
        print("Törölve.")
    else:
        print("Ezt már elhagytad!")

def minden_kipakolas():
    global hatizsak
    hatizsak = []

def main():
    kiir()
    hatizsak_feltoltes()
    kiir()
    kereses()
    kiir()
    rendrakas()
    kiir()
    eltavolitas()
    kiir()
    minden_kipakolas()
    kiir()

if __name__ == "__main__":
    main()