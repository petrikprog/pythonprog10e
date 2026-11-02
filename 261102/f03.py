import random

veletlenSzamList = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(veletlenSzamList)):
    veletlenSzamList[i] = random.randint(5,25)

print(veletlenSzamList)
print(veletlenSzamList[::-1])
print(veletlenSzamList[1::2])

index = -1
while True:
    index = int(input("Adj meg egy egész számot 1-10 között: "))
    if index >= 1 and index <= 10:
        break
    print("Helytelen érték")
print(veletlenSzamList[index-1])
