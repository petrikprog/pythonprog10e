print("1f")
szam1f = int(input("Szám 1-10: "))
for i in range(1, szam1f+1):
    print(f"{i}. fecske nem csinál nyarat")

print("2f")
szam2f = int(input("Szám 1-10:  "))
for i in range(1, szam2f+1):
    print(f"Megmondtam már {i}-szer, hogy semmit sem mondok el kétszer!")

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
