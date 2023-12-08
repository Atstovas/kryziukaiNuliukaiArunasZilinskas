# Kryžiukų ir nuliukų žaidimas
"""
1) tinkliukas - list masyvo su paspaustu skaičiumi -funkcija zaidejo interakcijai
2) seka - kito ėjimo metu priskirti kitą simbolį X arba O
3) zaidimo eiga - sąrašas kur saugomi ėjimai
4) render - zaidimo atvaizdavimas
4) new_render - naujo ėjimo atvaizdavimas
"""
import sys

zaidimo_eiga = []
render = {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-"}

def iseiti():
    print("klaida")
    sys.exit()

def klavisas(key):
    if int(key) < 1 or int(key) > 9:
        iseiti()
    skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
    return skaiciu_isdestymas[key]


def render_update(ejimas):
    if len(zaidimo_eiga) % 2 != 0:
        return render.update({ejimas: "O"})
    else:
        return render.update({ejimas: "X"})


def ciklas():
    ejimas = klavisas(input("ėjimas: "))
    return ejimas


def vaizdavimas():
    eilute1 = []
    eilute2 = []
    eilute3 = []
    for x, n in enumerate(render):
        if x > 5:
            if n == ejimas:
                if len(zaidimo_eiga) % 2 == 0:
                    eilute3.append("O")
                else:
                    eilute3.append("X")
            else:
                eilute3.append(render[n])
        elif x > 2:
            if n == ejimas:
                if len(zaidimo_eiga) % 2 == 0:
                    eilute2.append("O")
                else:
                    eilute2.append("X")
            else:
                eilute2.append(render[n])
        elif x >= 0:
            if n == ejimas:
                if len(zaidimo_eiga) % 2 == 0:
                    eilute1.append("O")
                else:
                    eilute1.append("X")
            else:
                eilute1.append(render[n])
    return eilute1, eilute2, eilute3

def patikra(zaidimo_eiga):
    if zaidimo_eiga[0] == 0 and zaidimo_eiga[2] == 1 and zaidimo_eiga[4] == 2:
        print("laimėjai")
        print(zaidimo_eiga)
        zaidimo_eiga = []
    if zaidimo_eiga[4] == 0 and zaidimo_eiga[5] == 1 and zaidimo_eiga[6] == 2:
        print("laimėjai")
        print(zaidimo_eiga)
        zaidimo_eiga = []
    return zaidimo_eiga

while True:
    ejimas = ciklas()
    render_update(ejimas)
    zaidimo_eiga.append(ejimas)
    vaizdas = vaizdavimas()
    print(zaidimo_eiga)
    print(vaizdas[0])
    print(vaizdas[1])
    print(vaizdas[2])
    print(render)
    # while True:
    #     if len(zaidimo_eiga) > 4:
    #         zaidimo_eiga = patikra(zaidimo_eiga)
    #         print("reset",zaidimo_eiga)
    #     break

