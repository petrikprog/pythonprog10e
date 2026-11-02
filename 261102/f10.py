import random
lista = []
for i in range(10):
    lista.append(random.uniform(-10,10))

for i in range(len(lista)):
    lista[i] = round(lista[i], 2)