lista1 = []
for i in range(10):
    lista1.append(i)

#jobbra
utolsoElem = lista1.pop()
lista1.insert(0, utolsoElem)

#balra
elsoElem = lista1.pop(0)
lista1.append(elsoElem)

