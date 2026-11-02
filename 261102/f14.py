lista = []
while 1:
    hova = ""
    while 1:
        hova = input("Hova szúrjuk be (\"eleje\", \"vége\"): ")
        if hova == "eleje" or hova == "vége":
            break
        print("HELYTELEN ÉRTÉK")
    szam = int(input("Számok (0 = vége): "))
    if szam == 0:
        print("VÉGE")
        break
    szerepel = False
    for i in range(len(lista)):
        if lista[i] == szam:
            print(f"A megadott szám már szerepel a listában. Index: {i}")
            szerepel = True
            break
    if szerepel:
        continue
    if hova == "eleje":
        lista.insert(0, szam)
    else:
        lista.append(szam)