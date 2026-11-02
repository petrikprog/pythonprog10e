import random

lista1 = []
lista2 = []

lista1Len = random.randint(1,100)
lista2Len = random.randint(1,100)
for i in range(lista1Len):
    lista1.append(random.uniform(1,100))

for i in range(lista2Len):
    lista2.append(random.uniform(1,100))

osszegLista = []

for i in range(max(lista1Len, lista2Len)):
    if lista1Len-1<i:
        osszegLista.append(lista2[i])
    elif lista2Len-1<i:
        osszegLista.append(lista1[i])
    else:
        osszegLista.append(lista1[i]+lista2[i])

