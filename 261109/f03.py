import random

jatekos_dobasok = [] #jatekosDobasok
gep_dobasok = [] #gepDobasok

jatekosDobasOsszeg = 0
gepDobasOsszeg = 0
for i in range(5):
    dobas = random.randint(1,6)
    jatekos_dobasok.append(dobas)
    jatekosDobasOsszeg += dobas

for i in range(5):
    dobas = random.randint(1,6)
    gep_dobasok.append(dobas)
    gepDobasOsszeg += dobas


jatekosPont = 0
gepPont = 0

for i in range(5):
    gepDobas = gep_dobasok[i]
    jatekosDobas = jatekos_dobasok[i]
    print(f"Dobás {i+1}. Gép: {gepDobas}, Játékos: {jatekosDobas}")
    if gepDobas > jatekosDobas:
        gepPont += 1
    elif gepDobas < jatekosDobas:
        jatekosPont += 1
    else:
        jatekosPont += 1
        gepPont += 1

print(f"Játékos pontszám: {jatekosPont}, Gép pontszám: {gepPont}")

if gepPont > jatekosPont:
    print("GÉP NYERT")
elif gepPont < jatekosPont:
    print("JÁTÉKOS NYERT")
else:
    print("DÖNTETLEN")