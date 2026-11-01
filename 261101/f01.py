height = 10
distance = 0
rebound = 0.8
numberOfRebounds = 0
requiredHeight = 0.01

while height > requiredHeight:
    distance += height
    numberOfRebounds += 1
    height *= rebound
    distance += height
print(f"{round(distance,2)} méter utat tett meg a labda, {numberOfRebounds} pattanás alatt.")
