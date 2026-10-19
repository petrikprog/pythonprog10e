import random
fordulokSzama = int(input("Fordulok szama: "))
aNyert = 0
bNyert = 0
dontetlen = 0
for i in range(fordulokSzama):
    aDobas = random.randint(1, 6)
    bDobas = random.randint(1, 6)
    print(f"{i+1}. fordulo: Anna: {aDobas}, Bela: {bDobas} - ", end="")
    if aDobas > bDobas:
        print("Anna nyert")
        aNyert+=1
    elif bDobas > aDobas:
        print("Bela nyert")
        bNyert+=1
    else:
        print("Dontetlen")
        dontetlen+=1
print(f"Anna: {aNyert} pont Bela: {bNyert} pont Dontetlenek: {dontetlen}")
print("A jatek gyoztese: ", end="")
if aNyert > bNyert:
    print("Anna")
elif bNyert > aNyert:
    print("Bela")
else:
    print("Dontetlen")
    
    