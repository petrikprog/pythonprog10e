import random

n = abs(int(input("Lista hossza: ")))
a = -1
b = -1

lista = []

while True:
    a = int(input("Intervallum a: "))
    b = int(input("Intervallum b: "))
    if a < b:
        break
    print("Az 'a'-nak kisebbnek kell lennie 'b'-nél")

for i in range(n):
    lista.append(random.randint(a, b))

for i in range(len(lista)):
    elem = lista[i]
    print(f"{i:^8}{elem:^8}",end="")
    if elem > 0:
        print(f"{"+":^8}")
    elif elem < 0:
        print(f"{"-":^8}")
    else:
        print(f"{"0":^8}")

while True:
    valasztas = input("a: Növelni; b: Csökkenteni; c: Szorozni; d: Kilépni\nVálasztás: ")
    if valasztas == "a":
        mertek = int(input("Mértek: "))
        for i in range(len(lista)):
            lista[i] += mertek
        print(lista)
    elif valasztas == "b":
        mertek = int(input("Mértek: "))
        for i in range(len(lista)):
            lista[i] -= mertek
        print(lista)
    elif valasztas == "c":
        mertek = int(input("Mértek: "))
        for i in range(len(lista)):
            lista[i] *= mertek
    elif valasztas == "d":
        print("KILÉPÉS")
        break
    else:
        print("HELYTELEN ÉRTÉK")