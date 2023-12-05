# Kryžiukų ir nuliukų žaidimas
"""
1) tinkliukas - list masyvo su paspaustu skaičiumi -funkcija zaidejo interakcijai
2) seka - kito ėjimo metu priskirti kitą simbolį X arba O
3) zaidimo eiga - sąrašas kur saugomi ėjimai
4) render - zaidimo atvaizdavimas
4) new_render - naujo ėjimo atvaizdavimas
"""

zaidimo_eiga = []

render = {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-"}


def klavisas(key):
    skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
    return skaiciu_isdestymas[key]

def render_update(ejimas):
    return render.update({ejimas: "X"})


ejimas = klavisas(input("ėjimas: "))
render_update(ejimas)
zaidimo_eiga.append(ejimas)

print(zaidimo_eiga)

eilute1 = []
eilute2 = []
eilute3 = []
for x, n in enumerate(render):
    if x > 5:
        if n == ejimas:
            eilute3.append("X")
        else:
            eilute3.append(render[n])
    elif x > 2:
        if n == ejimas:
            eilute2.append("X")
        else:
            eilute2.append(render[n])
    elif x >= 0:
        if n == ejimas:
            eilute1.append("X")
        else:
            eilute1.append(render[n])

print(eilute1)
print(eilute2)
print(eilute3)
print(render)

