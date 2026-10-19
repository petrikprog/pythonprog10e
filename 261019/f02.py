import random
randomSzam = random.randint(1, 100)
probSzama = 0
print("Gondoltam egy szamra 1 es 100 kozott.")
while True:
    tipp = int(input("Tipped: "))
    probSzama+=1
    if randomSzam > tipp:
        print("Nagyobbra gondoltam!")
    elif randomSzam < tipp:
        print("Kisebbre gondoltam!")
    else:
        print("Gratulalok! Eltalaltad!")
        break
print(f"Probalkozasok szama: {probSzama}")
    