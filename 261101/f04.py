num = 0
while True:
    num = int(input("Adj meg egy 3 jegyű egész számot: "))
    if num >= 100 and num <= 999:
        break
    print(f"Nem érvényes szám.")

numStr = str(num)
numStrReverse = numStr[::-1]

if numStr == numStrReverse:
    print(f"{num} szám palindrom")
else:
    print(f"{num} szám nem palindrom")

print("Palindromok: ")
for i in range(100, 1000):
    iStr = str(i)
    iStrReverse = iStr[::-1]
    if iStr == iStrReverse:
        print(i)