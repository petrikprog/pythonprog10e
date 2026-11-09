import random

szornyEtelek = ["kaja", "finom kaja", "nem finom kaja", "talán finom kaja", "talán nem finom kaja"]
titkosEtelIndex = random.randint(0, len(szornyEtelek)-1)
titkosEtel = szornyEtelek[titkosEtelIndex]

print(szornyEtelek)
talalt = False
for i in range(3):
    tipp = input("Mi a szörny kedvenc étele? ")
    if tipp == titkosEtel:
        print("A szörny megette az ételt és átengedett!")
        talalt = True
        break
    print("Nem talált!")
if not talalt:
    print("A szörny türelme elfogyott, elnyelt a sötétség!")