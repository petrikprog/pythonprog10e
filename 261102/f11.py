import random
lista = []
for i in range(10):
    lista.append(random.randint(-100,99))

print(lista)

for i in range(len(lista)):
    elem = lista[i]
    print(f"{i:^8}{elem:^8}",end="")
    if elem > 0:
        print(f"{"+":^8}")
    elif elem < 0:
        print(f"{"-":^8}")
    else:
        print(f"{"0":^8}")

for i in range(2, len(lista), 3):
    lista[i] += 1
print(lista)

for i in range(1, len(lista), 2):
    lista[i] -= lista[i-1]