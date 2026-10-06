import math
import random
# 1. feladat
print("1f")
szam1f = int(input("Szám 1-10: "))
for i in range(1, szam1f+1):
    print(f"{i}. fecske nem csinál nyarat")

# 2. feladat
print("2f")
szam2f = int(input("Szám 1-10:  "))
for i in range(1, szam2f+1):
    print(f"Megmondtam már {i}-szer, hogy semmit sem mondok el kétszer!")

# 3. feladat
print("3f")
for i in range(51):
    print(i)

for i in range(182,213):
    print(i)

for i in range(89, 56, -2):
    print(i)

for i in range(1, 21):
    print(i, i**2)

for i in range(99, 0, -3):
    print(i)

for i in range(101, 49, -5):
    print((i-1)*2)

for i in range(1, 1001):
    if i == 1000:
        print(f"{i}.")
    else:
        print(i, end=", ")

for i in range(1000,0,-3):
    print(i)

# 4. feladat
print("4f")
text = ""
for i in range(100):
    text+="*"
print(text)

karakter1 = input("Adj meg egy karaktert: ")
szamszor = int(input("Add meg h hányszor: "))
text = ""
for i in range(szamszor):
    text+=karakter1
print(text)

szoveg1 = input("Szöveg: ")
text = ""
for i in range(len(szoveg1)+2):
    text+="*"
print(text)
print(f"*{szoveg1}*")
print(text)


for i in range(8):
    text = ""
    space=True
    if i % 2 == 0:
        space=False
    for j in range(8):
        if not space:
            j+=1
        if j % 2 == 0:
            text += "*"
        else:
            text += " "
    print(text)

# 5. feladat
print("5f")
szam5f1 = int(input("Szám 1: "))
szam5f2 = int(input("Szám 2: "))
lepeskoz = int(input("Lépésköz: "))

if szam5f1 < szam5f2:
    for i in range(szam5f1, szam5f2+1, lepeskoz):
        print(i)
elif szam5f2 == szam5f1:
    print(szam5f1)
else:
    for i in range(szam5f1, szam5f2, -lepeskoz):
        print(i)

# 6. feladat
print("6f")
szam6f = int(input("Szám: "))
for i in range(1, szam6f+1):
    print(i**2, end=";")
print()

# 7. feladat
print("7f")
szam7f = int(input("Szám: "))
for i in range(1, szam7f+1):
    print(i**3)

# 8. feladat
print("8f")
a = 5
b = 21
for i in range(a, b+1):
    print(round(math.sqrt(i), 2))

# 9. feladat - math.factorial() 
print("9f")
szam9f = int(input("Szám: "))
runMult = 1
for i in range(1, szam9f+1):
    runMult *= i
print(runMult)

# 10. feladat - (6. feladat)
print("10f")
szam10f = int(input("Szám: "))
for i in range(1, szam10f+1):
    print(i**2)

# 11. feladat
print("11f")
szam11f = int(input("Szám: "))
runSum = 0
for i in range(1, szam11f, 2):
    runSum += i

print(runSum)

# 12. feladat
print("12f")
k = abs(int(input("Szám: ")))
sum12f = 0
for i in range(1, k+1):
    sum12f += i * (i+1)
print(sum12f)

# 13. feladat
print("13f")
n = abs(int(input("Szém: ")))
for i in range(3, n+1, 3):
    print(i)


# 14. feladat
print("14f")
szam14f = int(input("Szám: "))
fib = []
for i in range(szam14f+1):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-2] + fib[i-1])
    print(fib[i])

# 15. feladat
print("15f")
szam15f = int(input("Szám: "))
tesztelendo_szam = 1
talalt_szam = 0
while talalt_szam < szam15f:
    prime = True
    if tesztelendo_szam == 1:
        tesztelendo_szam+=1
        continue
    for j in range(2, int(math.sqrt(tesztelendo_szam))+1):
        if tesztelendo_szam % j == 0:
            prime=False
            break
    if prime:
        print(tesztelendo_szam)
        talalt_szam += 1
    tesztelendo_szam+=1

# 16. feladat
print("16f")
szam16f = int(input("Szám: "))
text="*\t"
for i in range(1, szam16f+1):
    text += f"{i:<10}"
print(text)
print(f" {"-"*szam16f*10}")
for i in range(1, szam16f+1):
    print(f"{i}|\t",end="")
    for j in range(1, szam16f+1):
        print(f"{i*j:<8}",end="  ")
    print()

# 17. feladt
print("17f")
print(random.randint(0, 10))
print(random.randint(0, 25))
print(random.randint(0, 50))
print(random.randint(10, 75))
print(random.randint(-50, 50))
print(random.randint(-100, -70))

# 18. feladat
print("18f")
szam18f = int(input("Szám: "))
csillag18f = f"{"*"*szam18f}"
print(csillag18f)
text = f"*{" "*(szam18f-2)}*"
for i in range(szam18f-2):
    print(text)
print(csillag18f)

# 19. feladat
print("19f")
m = int(input("M: "))
n = int(input("N: "))
text = f"{"*"*m}"
for i in range(n):
    print(text)

# 20. feladat
print("20f")
m20f = int(input("M: "))
n20f = int(input("N: "))
text = f"{"*"*m20f}"
for i in range(n20f):
    print(f"{" "*i}{text}")

# 21. feladat
print("21f")
n21f = int(input("N: "))
for i in range(n21f):
    print(f"{"*"*(2*i+1)}".center(n21f*2-1))

    
# 22. feladat
print("22f")
m22f = int(input("M: "))
n22f = int(input("N: "))
text = "*"*m22f
text2 = f"*{" "*(m22f-2)}*"
print(text)
for i in range(n22f-2):
    print(text2)
print(text)


# 23. feladta
print("23f")
feladat_ossz = int(input("Hány feladat? "))
ossz_valasz = feladat_ossz*2
jo_valasz = 0
for i in range(feladat_ossz):
    rand1 = random.randint(1,100)
    rand2 = random.randint(1,100)
    osszeg = rand1 + rand2
    kulonbseg = rand1 - rand2
    osszeg_input = int(input(f"{rand1}+{rand2}="))
    if osszeg == osszeg_input:
        print("Jó válasz")
        jo_valasz+=1
    else:
        print(f"Rossz válasz, a helyes válasz {osszeg}")
    kulonbseg_input = int(input(f"{rand1}-{rand2}="))
    if kulonbseg == kulonbseg_input:
        print("Jó válasz")
        jo_valasz+=1
    else:
        print(f"Rossz válasz, a helyes válasz {kulonbseg}")
print(f"{feladat_ossz}/{ossz_valasz}")


# 24. feladat
print("24f")
print(f"{"Kód":^10}{"Karakter":^10}")
for i in range(32, 256):
    char = chr(i)
    if char.isprintable():
        print(f"{i:^10}{char:^10}")

# 25. feladat
print("25f")
szam25f = abs(int(input("Szám: ")))
for i in range(1, szam25f):
    if szam25f % i == 0:
        print(i)

# 26. feladat
print("26f")
szam26f = abs(int(input("Szám: ")))
osszeg = 0
for i in range(1, szam26f+1):
    if szam26f % i == 0:
        osszeg += i
print(osszeg)


# 27. feladat
print("27f")
szam27f = abs(int(input("Szám: ")))
osszeg = 0
for i in range(1, szam27f+1):
    if szam27f % i == 0:
        osszeg += i
if szam27f*2 == osszeg:
    print("Tökéletes szám")
else:
    print("Nem tökéletes szám")

    
# 28. feladat
print("28f")
hatvanyalap = float(input("Hatványalap: "))
kitevo = float(input("Kitevő: "))
hatvanyertek = hatvanyalap**kitevo
print(hatvanyertek)


# 29. feladat
print("29f")
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(abc)):
    start = abc[i:26]
    end = abc[0:i]
    print(f"{start}{end}")
