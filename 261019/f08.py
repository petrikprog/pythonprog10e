import random
RED = "\033[0;31m"
DEFAULT = "\033[0m"
print(f"{RED}KINCSVADASZAT{DEFAULT}")
x = random.randint(1,10)
y = random.randint(1,10)
print(f"Talald meg a kincset! 7 probalkozasod van.")
kitalt = False
for i in range(7):
    print(f"{i+1}. probalkozas")
    xTipp = int(input("X koordinata: "))
    yTipp = int(input("Y koordinata: "))
    xTavolsag = abs(x-xTipp)
    yTavolsag = abs(y-yTipp)
    tavolsag = (xTavolsag**2 + yTavolsag**2)**0.5
    if tavolsag == 0:
        kitalt = True
        print(f"Gratulalok! Megtalaltad a kincset! Probalkozasok szama: {i+1}")
        break
    print(f"Tavolsag: {round(tavolsag, 2)}")
    if tavolsag <= 2:
        print("Forro!")
    elif tavolsag <= 5:
        print("Langyos!")
    else:
        print("Hideg!")
if not kitalt:
    print(f"Nem sikerult megtalalnod a kincset! Kincs koordinataja: ({x};{y}). Probalkozasok szama: 7")