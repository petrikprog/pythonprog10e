numOfBac = 1
multiplier = 2
maxBac = 100000
hours = 0
while numOfBac < maxBac:
    print(f"{hours}. óra: {numOfBac} baktérium")
    hours += 1
    numOfBac *= multiplier
print(f"{hours} óra elteltével {numOfBac} baktériumot értünk el.")