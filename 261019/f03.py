import random
fordulokSzama = int(input("Fordulok szama: "))
gepNyeres = 0
jatekosNyeres = 0
dontetlen = 0
for i in range(fordulokSzama):
    print(f"{i+1}. fordulo ", end="")
    gepValasztasa = random.randint(1,3)
    valasztas = int(input("Valasztasod (1-ko, 2-papir, 3-ollo): "))
    print(f"Gep valasztasa: {gepValasztasa} ", end="")
    if gepValasztasa == 1:
        print("(ko) ", end="")
        if valasztas == 1:
            print("Dontetlen!")
            dontetlen+=1
        elif valasztas == 2:
            print("Nyertel!")
            jatekosNyeres+=1
        else:
            print("A gep nyert!")
            gepNyeres += 1
    elif gepValasztasa == 2:
        print("(papir) ", end="")
        if valasztas == 1:
            print("A gep nyert!")
            gepNyeres += 1
        elif valasztas == 2:
            print("Dontetlen!")
            dontetlen+=1
        else:
            print("Nyertel!")
            jatekosNyeres+=1
    else:
        print("(ollo) ", end="")
        if valasztas == 1:
            print("Nyertel!")
            jatekosNyeres+=1
        elif valasztas == 2:
            print("A gep nyert!")
            gepNyeres+=1
        else:
            print("Dontetlen!")
            dontetlen+=1
print(f"Vegeredmeny: Jatekos {jatekosNyeres}, Gep {gepNyeres}, Dontetlen {dontetlen}")
        