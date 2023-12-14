# Kryžiukų ir nuliukų žaidimas
"""
0) pagal tinkliuką paskaičiuoja laimę
1) tinkliukas - list masyvo su paspaustu skaičiumi -funkcija zaidejo interakcijai
2) seka - kito ėjimo metu priskirti kitą simbolį X arba O
3) zaidimo eiga - sąrašas kur saugomi ėjimai
4) render - zaidimo atvaizdavimas
4) new_render - naujo ėjimo atvaizdavimas
"""
import sys
import os
import time

"GRID 3x3"
tinkliukas = 3
# tinkliukas = int(input("įvesk skaičių, kuris atspindės stulpelius ir eilutes pvz 3: "))
# print(f"Tinkliukas: {tinkliukas} x {tinkliukas}")
laime = []
listas = list(range(tinkliukas*tinkliukas))   #[0,1,2,3,4,5,6,7,8...]
eilute = []
stulp = []
stulp_n = []
istrizaines = []
istr = []

#eilutes [0,1,2],[3,4,5],[6,7,8]
for i in listas:
    if i % tinkliukas == 0:
        j = i + tinkliukas
        eilute.append(listas[i:j])
        laime.append(listas[i:j])

#stulpeliai [0,3,6],[1,4,7],[2,5,8]
for x,m in enumerate(eilute):
    for n in range(0,len(listas),tinkliukas):
        s = n + x
        stulp_n.append(s)
        #print(f"{n}-n; {x}-x; s=n+x {s}, stulp_n={stulp_n}")
    stulp.append(stulp_n)
    laime.append(stulp_n)
    stulp_n = []

#Įstrizaines[0,4,8],[2,4,6]
for m in range(tinkliukas):
    for n in eilute[m]:
        if n in stulp[m]:
            istr.append(n)
istrizaines.append(istr)
laime.append(istr)
istr = []
for m in range(tinkliukas):
    s = (m+1)*-1 # stulpialiu masyvas nuo galo [-1]
    for n in eilute[m]:
        if n in stulp[s]:
            istr.append(n)
istrizaines.append(istr)
laime.append(istr)
# print(istrizaines,"istrizaines")
# print(stulp, " stulpeliai")
# print(eilute, " eilutes")
# print(laime, "laimejimu sekos")

render = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}
#laime = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

zaidimo_eiga = []


def iseiti():
    print("Pabaiga")
    time.sleep(5)
    sys.exit()

def klavisas(key):
    if int(key) < 1 or int(key) > 9:
        iseiti()
    skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
    return skaiciu_isdestymas[key]

def klavisas_revers(key):
    skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
    return list(skaiciu_isdestymas.keys())[key]

def render_update(ejimas):
    if len(zaidimo_eiga) % 2 != 0:
        return render.update({ejimas: "O"})
    else:
        return render.update({ejimas: "X"})


def ciklas():

    if len(zaidimo_eiga) % 2 == 0:
        zaidejas = "X"
    else:
        zaidejas = "O"
    ejimas = klavisas(input(f"{zaidejas} ėjimas: "))
    if ejimas in zaidimo_eiga:
        print(f"klaida - {klavisas_revers(ejimas)}-langelis panaudotas ")
        if len(zaidimo_eiga) % 2 != 0:
            print("O -pralaimėjo")
        else:
            print("X -pralaimėjo")
        iseiti()
    os.system('cls')
    return ejimas


def vaizdavimas():
    eilute1 = []
    eilute2 = []
    eilute3 = []
    for x, n in enumerate(render):
        if x > 5: # 6,7,8 - duomenys atvaizdavimui apatinės eilutės
            if n == ejimas:
                if len(zaidimo_eiga) % 2 == 0:
                    eilute3.append("O")
                else:
                    eilute3.append("X")
            else:
                eilute3.append(render[n])
        elif x > 2:  # 5,4,3 - duomenys atvaizdavimui vidurinės eilutės
            if n == ejimas:
                if len(zaidimo_eiga) % 2 == 0:
                    eilute2.append("O")
                else:
                    eilute2.append("X")
            else:
                eilute2.append(render[n])
        elif x >= 0: # 0,1,2 - duomenys atvaizdavimui viršutinės eilutės
            if n == ejimas:
                if len(zaidimo_eiga) % 2 == 0:
                    eilute1.append("O")
                else:
                    eilute1.append("X")
            else:
                eilute1.append(render[n])
    return eilute1, eilute2, eilute3

def ekranas(): # spausdina render masyvus [render] per vaizdavimas() funkciją
    for n in range(3):
        print(vaizdas[n][0],"|",vaizdas[n][1],"|",vaizdas[n][2])
        print("---------")
    # print(vaizdas[0])
    # print(vaizdas[1])
    # print(vaizdas[2])

def patikra(zaidimo_eiga):
    patikra_x = [0]
    patikra_o = [0]
    for n in laime:
        for m in n:
            for i, x in enumerate(zaidimo_eiga):
                if x == m and i % 2 != 0:
                    patikra_o.append(1)
                elif x == m:
                    patikra_x.append(1)
        if len(patikra_x) == 4:
            ekranas()
            print("laimejo X")
            return iseiti()
        elif len(patikra_o) == 4:
            ekranas()
            print("laimejo O")
            return iseiti()
        else:
            patikra_x = [0]
            patikra_o = [0]

for n in range(3): # pirminis tinkliuko atvaizdavimas
    print(" ","|"," ","|"," ")
    print("---------")
while True:
    ejimas = ciklas() #klaviatūros įvestis
    render_update(ejimas) # kas antrą ėjimą grąžina X arba O
    zaidimo_eiga.append(ejimas)
    vaizdas = vaizdavimas()
    patikra(zaidimo_eiga)
    # print(zaidimo_eiga)
    ekranas()
    if len(zaidimo_eiga) == 9:
        print("lygiosios")
        iseiti()
    # print(render)


