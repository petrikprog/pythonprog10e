import random
lista = []
for i in range(10):
    lista.append(random.uniform(-10,10))

isLastPos = False
pozitivUtanNegativ = 0
for szam in lista:
    isPos = False
    if szam >= 0:
        isPos = True
    else:
        isPos = False
    if not isPos and isLastPos:
        pozitivUtanNegativ += 1
    isLastPos = isPos