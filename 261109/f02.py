felszerelesekList = ["kard", "gyógyital", "pajzs", "fáklya"]
print(felszerelesekList)

talaltTargy = input("Mit találtál a földön? ")

csere = False
while 1:
    valasztas = input("Le akarod-e cserélni valamelyik tárgyad? (igen, nem) ")
    if valasztas == "igen" or valasztas == "nem":
        if valasztas == "igen":
            csere = True
        break
    print("HELYTELEN ÉRTÉK")

if csere:
    while 1:
        csereIndex = int(input("Melyiket szeretnéd lecserélni? (0-3) "))
        if csereIndex <= 3 and csereIndex >= 0:
            felszerelesekList[csereIndex] = talaltTargy
            print(felszerelesekList)
            break
        print("HELYTELEN ÉRTÉK")
