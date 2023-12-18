# Kryžiukų ir nuliukų žaidimas
import sys
import os
import random

"GRID 3x3"
tinkliukas = 3 #by default
# tinkliukas = int(input("įvesk skaičių, kuris atspindės stulpelius ir eilutes pvz 3: "))
# print(f"Tinkliukas: {tinkliukas} x {tinkliukas}")
laime = [] # sugeneruojamos eilės tvarka eilutės, stulpeliai, įstrižainės
listas = list(range(tinkliukas*tinkliukas))   #[0,1,2,3,4,5,6,7,8...]
eilute = [] # sugeneruotos eilutės liste, kurios patalpintos liste [[]]
stulp = [] # sugeneruotos stulpeliai liste, kurie patalpinti liste [[]]
stulp_n = [] # vienas atskiras stulpelis kuris bus patalpintas į stulp = []
istrizaines = [] # įstrižainės
istr = [] # kiekviena atskira įstrižainė, kuri talpinama į istrizaines = []

#eilutes [0,1,2],[3,4,5],[6,7,8]
for i in listas: #[0,1,2,3,4,5,6,7,8...] # Tinkliukas = 3
    if i % tinkliukas == 0: # jeigu 0 / 3 == 0; ... ; jeigu 3 / 3 == 0; ... ; jeigu 6 / 3 == 0.
        j = i + tinkliukas # j=0+3 =>3; j=3+3 =>6; j=6+3 =>9;
        eilute.append(listas[i:j]) # Slices:#[0,1,2,3,4,5,6,7,8] => 0:3; 3:6; 6:9 rez:[0,1,2],[3,4,5],[6,7,8]
        laime.append(listas[i:j]) # sumuoja visas riekutes į laime[[0:3],[3:6],[6:9]]
        # laime = [[eilute0],[eilute1],[eilute2]]
#stulpeliai [0,3,6],[1,4,7],[2,5,8]
'''naudojamas eiučių skaičius kaip atskaitos taškas stulpeliams generuoti, bet pereita prie "tinkliukas" kintamojo
(supaprastinta for x,m in enumerate(eilutes) => nereikia "x" reikšmės "s" skaičiavimui ir enumerate funkcijos)'''
for m in range(tinkliukas): # 0,1,2 [išmokau enumerate'tinti ir per dažnai naudojau, ten kur nereikia]
    for n in range(0,len(listas),tinkliukas): #Range(0,9,3) nuo 0 iki 9 per žingsnį 3 [step 3]
        # print(m,n)
        s = m + n #["0",1,2,"3",4,5,"6",7,8] =>step3 ima nuo 1 kas trečią "n";
        # [s=0+0 =>0; s=0+3 =>3; s=0+6 =>6],[s=1+0 =>1; s=1+3 =>4; s=1+6=>7]...[]
        stulp_n.append(s) # [s] deda į listą n=0 [s] => n=3[s,s] => n=6[s,s,s]
        #print(f"{n}-n; {m}-x; s=n+x {s}, stulp_n={stulp_n}")
    stulp.append(stulp_n) # sudeda [s,s,s] [0,3,6].. kad gautume atskira stulpelių sąrašą (nereikalingas žingsnis)
    laime.append(stulp_n) # sudeda [s,s,s] į [laime]
    stulp_n = [] #nunulina eilučių sąrašą, kad galėtume formuoti kitas eilutes
    # laime = [[eilute0],[eilute1],[eilute2],[stulp0],[stulp1],[stulp2]]
#Įstrizaine[0,4,8] - manau galima optimizuoti, nes stulpelio ir eilutės susikirtimo reikšmių 'indeksai' vienodi.
#Ieškomas eilutės ir stulpelio susikirtimo taškas stulpeliai:['0',3,6],[1,'4',7],[2,5,'8']
for m in range(tinkliukas):# m = 0,1,2 in range(3)( eilutes: ['0',1,2],[3,'4',5],[6,7,'8'])
    for n in eilute[m]: #galimai galima apsiriboti vienu ciklu, nes n = 0,1,2,3,4,5,6,7,8
        #print(m,n)
        # for 0 in eilute[0] =>iš [0,1,2] ištraukiam 0 ir "if'as" suranda stulp[0] skaiciu 0
        # for 1 in eilute[0] =>iš [0,1,2] ištraukiam 1 ir "if'as" - neranda sekoje stulp[0] => [0,3,6]
        # for 2 in eilute[0] =>iš [0,1,2] ištraukiam 2 ir "if'as" - neranda sekoje stulp[0] => [0,3,6]
        # for 3 in eilute[1] =>iš [3,4,5] ištraukiam 3 ir "if'as" - neranda sekoje stulp[1] => [1,4,7]
        # for 4 in eilute[1] =>iš [3,4,5] ištraukiam 4 ir "if'as" suranda stulp[1] skaiciu 4
        # for 5 in eilute[1] =>iš [3,4,5] ištraukiam 5 ir "if'as" - neranda sekoje stulp[1] => [1,4,7]
        # for 6 in eilute[2] =>iš [6,7,8] ištraukiam 6 ir "if'as" - neranda sekoje stulp[2] => [2,5,8]
        # for 7 in eilute[2] =>iš [6,7,8] ištraukiam 7 ir "if'as" - neranda sekoje stulp[2] => [2,5,8]
        # for 8 in eilute[2] =>iš [6,7,8] ištraukiam 8 ir "if'as" suranda stulp[2] skaiciu 8
        if n in stulp[m]: # ieškomas eilutės[0]= [0,1,2] ir stulpelio[0]= [0,3,6] susikirtimo taškas
            istr.append(n) #surastas reikšmes dedam į laikiną listą, kurį nunulinsim ir naudosim kitai įstrižainei
istrizaines.append(istr) #Įstrizaine[0,4,8]
laime.append(istr)
# laime = [[eilute0],[eilute1],[eilute2],[stulp0],[stulp1],[stulp2],[įstriž1]]
istr = []
#Įstrizaine [2,4,6] viskas kaip su pirma įstrižaine tik pridėtas s - kintamasis
#Veidrodinis variantas, kuris įgyvendintas su s-kintamuoju
for m in range(tinkliukas):
    s = (m+1)*-1 # stulpeliu masyvas nuo galo [-1]
    for n in eilute[m]:
        if n in stulp[s]:
            istr.append(n)
istrizaines.append(istr)
laime.append(istr)
# laime = [[eilute0],[eilute1],[eilute2],[stulp0],[stulp1],[stulp2],[įstriž0],[įstriž1]]
# print(istrizaines,"istrizaines")
# print(stulp, " stulpeliai")
# print(eilute, " eilutes")
# print(laime, "laimejimu sekos")

skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
render = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

#laime = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


suvestine = []
zaidimo_eiga = []
bot = False

def botas():
    x = random.randrange(9)
    if len(zaidimo_eiga) == 1:
        if render[4] == "X":
            ejimas = "7"
            return skaiciu_isdestymas[ejimas]
    if render[4] == " ":
        ejimas = "5"
        return skaiciu_isdestymas[ejimas]
    for r in range(6):
        if render[x] == " ":
            return skaiciu_isdestymas[klavisas_revers(x)]
    for n in render:
        if render[n] == " ":
            #return skaiciu_isdestymas[list(skaiciu_isdestymas.keys())[n]]
            return skaiciu_isdestymas[klavisas_revers(n)]

def valyti():
    global render, zaidimo_eiga, vaizdas
    render = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}
    zaidimo_eiga = []
    vaizdas = [' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']
    os.system('cls')

def iseiti(laimetojas=""):
    # print("Pabaiga")
    global bot
    if laimetojas != "":
        suvestine.append(laimetojas)
    while True:
        try:
            meniu = int(input("Žaisti dviems     = 1\n"
                          "Sesijos suvestinė = 2\n"
                          "Išeiti            = 3\n"
                          "Žaisti prieš PC   = 4\n"))
            if meniu not in range(1,5):
                continue
            break
        except:
            print("Išimtis")
    match meniu:
        case 1:
            bot = False
            valyti() #kartoti
        case 2:
            #suvestinė
            sarasas = ""
            x = []
            o = []
            lyguma = []
            for win in suvestine:
                sarasas = sarasas +" "+str(win)
                if win == "=":
                    lyguma.append(win)
                elif win == "X":
                    x.append(win)
                elif win == "O":
                    o.append("O")
            print("Žaidimo sesijos rezultatų seka :",sarasas)
            print(f"X laimėjo {len(x)}-kart")
            print(f'O laimėjo {len(o)}-kart')
            print(f'{len(lyguma)}-kart lygiosiomis')
            print("----------------------")
            iseiti()
        case 3:
            sys.exit() #Exit
        case 4:
            bot = True
            valyti() #Žaisti prieš PC (bot == True)

def klavisas():
    # skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
    if len(zaidimo_eiga) % 2 == 0:
        zaidejas = "X"
    else:
        if bot == True:
            return botas()
        else:
            zaidejas = "O"
    while True:
        try:
            ejimas = input(f"{zaidejas} ėjimas: ")
            x = skaiciu_isdestymas[ejimas]
            # print(bot,"while viduje")
            if render[x] == "X" or render[x] == "O":
                continue
            break
        except KeyError:
            print("pakartok 1-9 intervale")
            continue
    return skaiciu_isdestymas[ejimas]

def klavisas_revers(key):
    # skaiciu_isdestymas = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}
    return list(skaiciu_isdestymas.keys())[key]

def render_update(ejimas):
    if len(zaidimo_eiga) % 2 != 0:
        return render.update({ejimas: "O"})
    else:
        return render.update({ejimas: "X"})


def ciklas():
    ejimas = klavisas()
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
        if n != 2:
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
            return iseiti("X")
        elif len(patikra_o) == 4:
            ekranas()
            print("laimejo O")
            return iseiti("O")
        else:
            patikra_x = [0]
            patikra_o = [0]

def pirminis():
    for n in range(3): # pirminis tinkliuko atvaizdavimas (vienkartinis)
        print(" ","|"," ","|"," ")
        if n != 2:
            print("---------")
iseiti()
pirminis()
while True:
    ejimas = ciklas() #klaviatūros įvestis
    render_update(ejimas) # kas antrą ėjimą grąžina X arba O
    zaidimo_eiga.append(ejimas)
    a = render # 9 langeliai neUNIVERSALU
    b = zaidimo_eiga # pradžioje tuščias masyvas
    vaizdas = vaizdavimas() #spausdina tris eilutes neUNIVERSALU
    patikra(zaidimo_eiga)
    # print(zaidimo_eiga)
    ekranas() #neUNIVERSALU
    if len(zaidimo_eiga) == 9:
        print("lygiosios")
        iseiti("=")
    # print(render)


