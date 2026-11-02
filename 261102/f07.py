import random

n = abs(int(input("Lista hossza: ")))
listN = []
for i in range(n):
    listN.append(random.uniform(1,10))

osszeg = 0
for szam in listN:
    osszeg += szam