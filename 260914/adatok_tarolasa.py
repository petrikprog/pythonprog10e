print("Hello, ma az adatok tárolását tanuljuk meg :)")

#tipusok: egész: int, valós: float, szöveges: str, karakter: char, logikai: bool

nev = "Máté"
nev = "MÁTÉ"
print(f"Hello {nev}!")
print(type(nev))

#egész
egesz = 16
print(f"Az egész változó típusa {type(egesz)}, értéke pedig: {egesz}")
#valós
valos = 32.5 #valos tizedespontot használ
print(f"A valós változó típusa {type(valos)}, értéke pedig: {valos}")

logikai = True
print(f"A logikai értéke {logikai}, tipusa: {type(logikai)}")

karakter = '='
print(karakter, type(karakter))

stars = (len(nev)+2)*'*'
print(stars)
print(f"*{nev}*")
print(stars)