# Kryžiukų ir nuliukų žaidimas
"""
1) tinkliukas - list masyvo su paspaustu skaičiumi -funkcija zaidejo interakcijai
2) seka - kito ėjimo metu priskirti kitą simbolį X arba O
3) zaidimo eiga - sąrašas kur saugomi ėjimai
4) render - zaidimo atvaizdavimas
4) new_render - naujo ėjimo atvaizdavimas
"""

tinkliukas = ["0", "1", "2", "3", "4", "5", "6", "7", "8","9"]
zaidimo_eiga = ["5","3"]
seka =  ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
# render = [["7","8","9"],["4","5","6"],["1","2","3"]]
render = [["7","8","9"],["4","X","6"],["1","2","O"]]
render_1 = ["7","8","9","4","5","6","1","2","3"]

def klavisas(key):
    skaiciu_isdestymas = {"7":0,"8":1,"9":2,"4":3,"5":4,"6":5,"1":6,"2":7,"3":8}
    return skaiciu_isdestymas[key]

zaidimo_eiga.append(klavisas("7"))
print(zaidimo_eiga)
tinkliukas_2 = {"0":"-","1":"-","2":"-","3":"-","4":"-","5":"-","6":"-","7":"-","8":"-"}



new_render = []

for x,n in enumerate(render):
    print(n)
    for m in n:
        # print(m,x)
        if m == "X":
            new_render.append("X")
        elif m == "O":
            new_render.append("O")
        else:
            new_render.append("-")

print('--------')
print(new_render)
print('--------')
eilute1 = []
eilute2 = []
eilute3 = []

for x,n in enumerate(new_render):
    if x > 5:
        eilute3.append(n)
    elif x > 2:
        eilute2.append(n)
    elif x >= 0:
        eilute1.append(n)

print(eilute1)
print(eilute2)
print(eilute3)