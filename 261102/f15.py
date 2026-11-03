import random
lista = []
for i in range(20):
    lista.append(random.randint(0,100))

print(lista)
i = 0
while i < len(lista):
    szam = lista[i]
    if szam > 50 and szam % 2 == 0:
        lista.remove(szam)
    else:
        i+=1
print(lista)

paratlanLista = []
i = 0
while i < len(lista):
    szam = lista[i]
    if szam % 2 == 1:
        paratlanLista.append(szam)
        lista.remove(szam)
    else:
        i+=1
print(lista)
print(paratlanLista)
ketjegyuSzamokSzama = 0
for szam in lista:
    if szam >= 10 and szam <= 100:
        ketjegyuSzamokSzama+=1
print(f"Az eredeti listában {ketjegyuSzamokSzama} kétjegyű szám van.")