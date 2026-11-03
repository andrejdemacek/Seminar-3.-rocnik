#vypis cisla od 1 do 20 a jeho vzajomne nasobky
for i in range(1,21):
    print(f"{i} {i*i}")

a = 1
while a < 21:
    print(a , a * a)
    a += 1

b = 0
pocet = 0
while b < 101:
    b = int(input("Zadaj cislo: "))
    pocet += 1
    print("Pocet nacitanych cisel:" , pocet)

c = int(input("Zadaj cislo: "))
while c < 101:
    print(c)
    c += 1

sucet = 0
p = 0
while sucet < 101:
    k = int(input("Zadaj cislo: "))
    sucet += k
    print("Sucet je:" , sucet)
    p += 1
    print("Pocet nacitanych cisel:" , p)

#v cykle nacitavaj mena a v kazdom vypis pocet jeho znakov
meno = ""
while meno != "koniec":
    meno = str(input("Zadaj meno: "))
    if meno != "koniec":
        print(len(meno))

#napis program ktory nacita meno pouzivatela pomocou funkcie len zisti pocet
name = str(input("Zadaj meno: "))
pocet = len(name)
print(f"Tvoje meno ma {pocet} znakov.")

podlazie = 0
osoby = 2
while osoby < 10:
    osoby += 3
    podlazie += 1
print(f"Podlazie: {podlazie}\nOsoby: {osoby}")

poschodie = 0
while poschodie < 7:
    poschodie += 1
    print(f"poschodie: {poschodie}")
print("Vytah zastavil.")

pocet_osob = 0
kg = 0
max_kg = 400
while kg < max_kg:
    clovek_kg = int(input("Zadaj hmotnost cloveka: "))
    kg += clovek_kg
    pocet_osob += 1
    print(f"Hmotnost ludi dokopy: {kg}")
    print(f"Pocet osob:{pocet_osob}")
print("Vytah presiahol nosnost.")

import random
osoba_kg = 0
pocet_osob = 0
kg = 0
max_kg = 400
while kg < max_kg:
    osoba_kg = random.randint(50, 100)
    pocet_osob += 1
    print(f"{pocet_osob}. osoba ma hmotnost: {osoba_kg}")
    kg += osoba_kg
    print(f"Hmotnost ludi dokopy: {kg}")
    print(f"Pocet osob:{pocet_osob}")
print("Vytah presiahol nosnost.")

import random
interval_min = int(input("Zadaj najmensie cislo intervalu: "))
interval_max = int(input("Zadaj najvacsie cislo intervalu: "))
cislo = int(input(f"Zadaj cislo ktore program uhadne od {interval_min} do {interval_max}: "))
tip = 0
if cislo < interval_min or cislo > interval_max or interval_max > interval_max:
    if cislo < interval_min or cislo > interval_max:
        print("cislo nie je v intervale")
    else:
        print("zadali ste interval naopak")
else:
    while tip != cislo:
        tip = random.randint(interval_min, interval_max)
        print(tip)
    print(f"pocitac uhadol cislo: {tip}")

cislo = int(input("Zadaj cislo: "))
sucet = 0
while cislo > 0:
    cifra = cislo % 10
    sucet += cifra
    cislo //= 10
print(f"Sucet cifier je {sucet}.")

#len parne
cislo = int(input("Zadaj cislo: "))
sucet = 0
while cislo > 0:
    cifra = cislo % 10
    if cislo % 2 == 0:
        sucet += cifra
    cislo //= 10
print(f"Sucet cifier je {sucet}.")

import math
cislo = int(input("Zadaj cislo: "))
delitele = 0
for i in range(2, int(math.sqrt(cislo))):
    if cislo % i == 0:
        delitele += 1
        print("Nie je to prvocislo.")
        break
if delitele == 0:
    print("Prvocislo ako repa.")

#1
cislo = abs(int(input("Zadaj cislo: ")))
cif_sucet = 0
while cislo > 0:
    cifra = cislo % 10
    cif_sucet += cifra
    cislo //= 10
print(f"Ciferny sucet je {cif_sucet}.")

#2
cislo = abs(int(input("Zadaj cislo: ")))
pocet_parnych_cifier = 0
while cislo > 0:
    cifra = cislo % 10
    if cifra % 2 == 0:
        pocet_parnych_cifier += 1
    cislo //= 10
print(f"Pocet parnych cifier je {pocet_parnych_cifier}.")

#3
cislo = abs(int(input("Zadaj cislo: ")))
pocet_cifier = 0
while cislo > 0:
    cifra = cislo % 10
    pocet_cifier += 1
    cislo //= 10
print(f"Pocet cifier je {pocet_cifier}.")

#4
cislo = int(input("Zadaj cislo: "))
cislo_povodne = cislo
cislo = abs(cislo)
cislo_otocene = 0
while cislo > 0:
    cifra = cislo % 10
    cislo_otocene = cislo_otocene * 10 + cifra
    cislo //= 10
if cislo_povodne < 0:
    cislo_otocene = -cislo_otocene
    print(f"Cislo {cislo_povodne} odzadu je {cislo_otocene}.")
else:
    print(f"Cislo {cislo_povodne} odzadu je {cislo_otocene}.")

#5
cislo = abs(int(input("Zadaj cislo: ")))
parne_miesta = 0
neparne_miesta = 0
pozicia = 1
while cislo > 0:
    cifra = cislo % 10
    if pozicia % 2 == 0:
        parne_miesta = parne_miesta * 10 + cifra
    else:
        neparne_miesta = neparne_miesta * 10 + cifra
    cislo //= 10
    pozicia += 1
print(f"Parne miesta odzadu: {parne_miesta}")
print(f"Neparne miesta odzadu: {neparne_miesta}")

#5A
cislo = abs(int(input("Zadaj cislo: ")))
parne_cifry = 0
neparne_cifry = 0
pozicia = 1
while cislo > 0:
    cifra = cislo % 10
    if pozicia % 2 == 0:
        parne_cifry = parne_cifry * 10 + cifra
    else:
        neparne_cifry = neparne_cifry * 10 + cifra
    cislo //= 10
    pozicia += 1
parne_spravne = 0
while parne_cifry > 0:
    cifra = parne_cifry % 10
    parne_spravne = parne_spravne * 10 + cifra
    parne_cifry //= 10
neparne_spravne = 0
while neparne_cifry > 0:
    cifra = neparne_cifry % 10
    neparne_spravne = neparne_spravne * 10 + cifra
    neparne_cifry //= 10
print(f"Parne cifry: {parne_spravne}")
print(f"Neparne cifry: {neparne_spravne}")

#6
cislo = abs(int(input("Zadaj cislo: ")))
cislo_povodne = cislo
pocet = 0
if cislo_povodne == 0:
    pocet = 1
else:
    while cislo_povodne > 0:
        pocet += 1
        cislo_povodne //= 10
if pocet % 2 == 0:
    k = pocet // 2 - 1
    cislo_povodne = cislo
    for _ in range(k):
        cislo_povodne //= 10
    druha_stredna = cislo_povodne % 10
    cislo_povodne //= 10
    prva_stredna = cislo_povodne % 10
    priemer = (prva_stredna + druha_stredna) / 2.0
    print(f"Priemer dvoch strednych cifier je {priemer}.")
else:
    k = pocet // 2
    cislo_povodne = cislo
    for _ in range(k):
        cislo_povodne //= 10
    stredna = cislo_povodne % 10
    print(f"Stredna cifra je {stredna}.")

#7
cislo = int(input("Zadaj cislo v desiatkovej sustave: "))
if cislo == 0:
    vysledok = 0
else:
    vysledok = 0
    mocnina = 1
    cislo_povodne = abs(cislo)
    while cislo_povodne > 0:
        vysledok += (cislo_povodne % 2) * mocnina
        mocnina *= 10
        cislo_povodne //= 2
    if cislo < 0:
        vysledok = -vysledok
print(f"Dvojkova sustava: {vysledok}")

#8
cislo = abs(int(input("Zadaj cislo v dvojkovej sustave (iba 0 a 1): ")))
vysledok = 0
mocnina = 1
while cislo > 0:
    vysledok += (cislo % 10) * mocnina
    mocnina *= 2
    cislo //= 10
print(f"Desiatkova sustava: {vysledok}")

#9
cislo = abs(int(input("Zadaj cislo: ")))
cislo_povodne = cislo
cislo_otocene = 0
while cislo > 0:
    cifra = cislo % 10
    cislo_otocene = cislo_otocene * 10 + cifra
    cislo //= 10
if cislo_povodne == cislo_otocene:
    print(f"Cislo {cislo_povodne} je palindrom. ({cislo_povodne} = {cislo_otocene})")
else:
    print(f"Cislo {cislo_povodne} nie je palindrom. ({cislo_povodne} != {cislo_otocene})")

#10
import math
cislo = int(input("Zadaj cislo: "))
delitele = 0
for i in range(2, int(math.sqrt(cislo))):
    if cislo % i == 0:
        delitele += 1
        print("Nie je to prvocislo.")
        break
if delitele == 0:
    print("Prvocislo ako repa.")

#11
n = int(input("Zadaj cislo: "))
print("Prvociselny rozklad:", end=" ")
if n < 2:
    print("Zadane cislo nema prvociselny rozklad.")
else:
    d = 2
    prvy = True
    while n > 1:
        while n % d == 0:
            if not prvy:
                print(" * ", end="")
            print(d, end="")
            prvy = False
            n //= d
        d += 1
    print()

#12
n = abs(int(input("Zadaj cislo: ")))
print("Delitelia cisla:", end=" ")
d = 1
while d <= n:
    if n % d == 0:
        print(d, end=" ")
    d += 1
print()

#13
n = int(input("Zadaj cislo: "))
print("Collatzova postupnost:", end=" ")
while n > 1:
    print(n, end=", ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)

from random import randint as rnd
while True:
    cislo = int(rnd(0, 50))
    if cislo != 0:
        if cislo % 2 == 0:
            print(f"Cislo {cislo} je parne.")
        else:
            print(f"Cislo {cislo} je neparne.")
    else:
        print("Padla 0.")
        break

from random import randint as rnd
while True:
    a = int(rnd(1, 20))
    b = int(rnd(1, 20))
    if a == b:
        print(f"cislo {a} = cislo {b}")
        break
    elif a > b:
        print(f"cislo {a} > cislo {b}")
    else:
        print(f"cislo {a} < cislo {b}")

from random import randint as rnd
print(end = "")
pocet = 0
a/m = input('Zadaj "a" (automaticke) alebo "m" (manualne(enterom po jednom)).') 
while True:
    a, b, c = [int(rnd(0, 10)), int(rnd(0, 10)), int(rnd(0, 10))]
    if a/m == "a":
        print()
    elif a/m == "m":
        input()
    else:
        print("Neznama hodnota")
        break
    if a == 7 and b == 7 and c == 7:
        print()
        print("*" * 7,)
        print(f"*{a},{b},{c}*")
        print("*" * 7)
        print(f"Prehal si {pocet}-krat.")
        print()
        break
    else:
        print(f"{a},{b},{c}", end = "")
        pocet += 1
