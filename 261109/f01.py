import random

kincsLista = ["~", "~", "~", "~", "~"]

kincsIndex = random.randint(0, len(kincsLista)-1)
kincsLista[kincsIndex] = "X"

tipp = -1

while 1:
    tipp = int(input("Hol van a kincs 0-4: "))
    if tipp <= 4 and tipp >= 0:
        break
    print("HELYTELEN ÉRTÉK")

if kincsIndex == tipp:
    print("Gratulálok, megtaláltad az aranyat!")
else:
    print("Sajnos itt csak hullámok vannak...")
    print(kincsLista)