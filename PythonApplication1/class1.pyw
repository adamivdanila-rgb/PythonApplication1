class my_class(object):
    pass# T�� 3.1
#1. Sisesta, mitu neist on t�isarvud.
##k=0 # loendur
for i in range(15):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1}. arv: "))
            break
        except:
            print("Vale andmet��p!")

    if int(arv)==arv:
        print(f"{arv} on t�isarv")
        K = 0  # defineeri muutuja enne kasutamist
arv = float(input("Sisesta 1. arv: "))
if arv == int(arv):
    print(f"{arv} on t�isarv")
    K += 1
print(f"T�isarve oli kokku {k} tk")
#2. K�si kasutajalt arv A ja
#leia k�igi naturaalarvude summa vahemikus 1 kuni A.
s=0 #Summa
while True:
    try:
        A=int(input(f"Sisesta A: "))
        break
    except:
        print("Vale andmet��p!")
for i in range(1,A+1):
    s=s+i
print(f"Summa vahemikus 1 kuni {A} v�rdub {s}")

#3. Sisestatakse 8 arvu.
#Leida nende korrutis (ainult positiivsete arvude puhul).
korrutis=1
for i in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1}. arv: "))
            if arv<0: break
        except:
            print("Vale andmet��p!")
    korrutis*=arv
print(f"Korrutis v�rdub {korrutis}")


#4. Koosta proframm
#mis v�ljastab ekraanile arvude ruudud vahemikus 10 kuni 20.

for i in range(10,21):
    print(f"Arv {i} ruut on {i**2}")

#5. Koosta programm
#mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
#N v��rtus sisestatakse klaviatuurilt.
#Isaseisvalt






