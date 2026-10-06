
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