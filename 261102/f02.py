import random

veletlenList = []
for i in range(7):
    veletlenList.append(bool(random.randint(0,1)))

for i in range(len(veletlenList)):
    if veletlenList[i]:
        print("IGAZ")
    else:
        print("HAMIS")