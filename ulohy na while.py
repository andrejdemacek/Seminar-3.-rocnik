
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
