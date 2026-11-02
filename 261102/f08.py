import random
lista = []
for i in range(10):
    lista.append(random.uniform(1,10))

listaLen = len(lista)
for i in range(0,listaLen,2):
    if i+1 <= listaLen-1:
        lista[i] += lista[i+1]
