lista = ["alma","körte","őszibarack","sárgabarack","szilva","málna","áfonya"]
szoveg = ""
for i in range(len(lista)):
    if i != 0:
        szoveg += ","
    szoveg += lista[i]