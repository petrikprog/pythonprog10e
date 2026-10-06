import random
#for ismétel: annyiszor fut le az utasitás, ahányszor range-ben meghatározom
#range(5)

for i  in range(5):#i étékei 0-tól 4-ig. Az 5-ot már nem veszi fel az i
    print(i) #ciklusmag: bármennyi utasitás lehet benne. Amit egy tabulátorral bentebb rakunk, azt ismétli
#i értéke 1-től 5-ig veszi fel
for i in range(1,6): # az i utolsó értéke: 5
    print(i)
print("-------------------------------------")    
for makimajom in range(10):
    print(makimajom, end = ", ") #end: felülirjuk a sor végi entert egy vessző space kombóra, igy nem egymás alá kerülnek, hanem egymás mellé
print() # egyszerű sortörés, hogy ne ugyanabba a sorba folytassuk a kiirást
print(f"Az i értéke: {i}")
print(f"Az makimajom értéke: {makimajom}")

#pozitív egyjegyű páratlan számok 
for i in range(1,10,2):
    print(i, end = " ")
print()

#pozitív egyjegyű páros számok 
for i in range(2,10,2):
    print(i, end = " ")
print()

#10-nél kisebb egyjegyű primszámok: 
print("Primszámok: ", end = "")
for i in range(2,10):
    prime= True
    #primszám: ha egyel és önmagával osztható csak
    for j in range(2,i): # amig a belső ciklus le nem fut a külső ciklus nem lép tovább
        if i%j == 0:
            prime = False

    if prime:
        print(i, end = ", ")

#lottószámok generálása: 5-ös lottó
print()
for i in range(1,6):
    veletlen = random.randint(1,90)
    print(f"{i}. lottószám: {veletlen}")

#hatos: 1-45 6 szám
print()
for i in range(1,7):
    veletlen = random.randint(1, 45)
    print(f"{i}. lottószám: {veletlen}")
#skandinav: 1-35 7 szám
print()
for i in range(1,8):
    veletlen = random.randint(1,35)
    print(f"{i}. lottószám: {veletlen}")