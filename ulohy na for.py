#1
for i in range(11):
    print(i)

#2a
a = int(input("Zadaj cislo: "))
for i in range(1, a + 1):
    print(i)

#2b
b = int(input("Zadaj cislo: "))
for i in range (1,b + 1):
    if i == b:
        print(i,end = ".")
    else:
        print(i,end = ",")
print()

#3
c = int(input("Zadaj cislo: "))
for i in range(5,c + 1,2):
    if i == c:
        print(i, end=".")
    else:
        print(i, end=",")
print()

#4
d = int(input("Zadaj cislo: "))
for i in range(1,d + 1):
    print(f"{i} {i**2}")

#5
import math
zaciatok = int(input("Zadaj prve cislo: "))
koniec = int(input("Zadaj posledne cislo: "))
for i in range(zaciatok, koniec + 1):
    odmocnina = round(math.sqrt(i), 2)
    print(f"{i} {odmocnina}")

#6
for x in range(1, 21):
    if x == 3:
        print("Funkcia nie je definovana.")
    else:
        y = (x**2 - 1) / (x - 3)
        print(f"x = {x} y= {y}")

#7
e = int(input("Zadaj cislo: "))
for i in range(1,e + 1):
    if i % 3 == 0:
        print(i)

#8
for i in range(2,21,2):
    print(i)
#9
z = int(input("zadaj prve cislo: "))
k = int(input("zadaj posledne cislo: "))
for i in range(z,k + 1):
    if i % 2 != 0:
        print(i)
#10
f = int(input("Zadaj cislo: "))
for i in range(f, 0, -1):
        if i == 1:
            print(i)
        else:
            print(i, end=",")
print()