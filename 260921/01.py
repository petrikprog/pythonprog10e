nev = "Katalin"
megszolitas = "Mrs."
cimzett = megszolitas + nev

print(cimzett)

# hossz = len()
print(len(cimzett))

# hivatkozas elemre [sorszam]
print(cimzett[0])

# kivagas [elsoElem:utolsoElem]
print(cimzett[1:5])

# levagas üresen hagyott karaktertől
print(cimzett[:3])
print(cimzett[3:])
print(cimzett[-1])

# bool
valasz = True
nevalasz = False
print(valasz)

# reláció
valasz = 3 > 4
print(valasz)
print(type(valasz))

# relációk: <, >, ==, <=, >=, !, !=
# logikai:  ! (not), OR, AND
# elagazas - IF
egyik = 5
masik = 10

if egyik > masik:
    print(f"Az {egyik} nagyobb mint a {masik}")
# kétirányú elágazás If - else
else:
    print(f"Az {egyik} kisebb mint a {masik}")

kor = 21

if kor >= 18:
    print("Vehet energiaitalt")
else:
    print("Nem vehet energiaitalt")

szam = int(input("Adjon meg egy számot: "))
if szam > 0:
    print("pozitív szám")
elif szam < 0:
    print("negatív szám")
else:
    print("nulla")

# Logikai függvények
elso = True
masodik = False
print(elso or masodik)
print(elso and masodik)
print(not masodik and elso)