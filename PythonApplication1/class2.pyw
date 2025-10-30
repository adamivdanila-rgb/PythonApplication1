# Töö 3.1
#1. Sisesta, mitu neist on täisarvud.
##k=0 # loendur
# for i in range(15):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1}. arv: "))
#             break
#         except:
#             print("Vale andmetüüp!")

#     if int(arv)==arv:
#         print(f"{arv} on täisarv")
#         K = 0  # defineeri muutuja enne kasutamist
# arv = float(input("Sisesta 1. arv: "))
# if arv == int(arv):
#     print(f"{arv} on täisarv")
#     K += 1
# print(f"Täisarve oli kokku {k} tk")
# #2. Küsi kasutajalt arv A ja
# #leia kõigi naturaalarvude summa vahemikus 1 kuni A.
# s=0 #Summa
# while True:
#     try:
#         A=int(input(f"Sisesta A: "))
#         break
#     except:
#         print("Vale andmetüüp!")
# for i in range(1,A+1):
#     s=s+i
# print(f"Summa vahemikus 1 kuni {A} võrdub {s}")

# #3. Sisestatakse 8 arvu.
# #Leida nende korrutis (ainult positiivsete arvude puhul).
# korrutis=1
# for i in range(8):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1}. arv: "))
#             if arv<0: break
#         except:
#             print("Vale andmetüüp!")
#     korrutis*=arv
# print(f"Korrutis võrdub {korrutis}")


#4. Koosta proframm
#mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.

# for i in range(10,21):
#     print(f"Arv {i} ruut on {i**2}")

#5. Koosta programm
#mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
#N väärtus sisestatakse klaviatuurilt.
#Isaseisvalt





#3. variant
#Väljasta naturaalarvude astmed, mis ei ületa arvu n³.
#Kasutaja määrab astme näitaja ja arvu n.

# n = int(input("Sisesta arv n: "))
# m = int(input("Sisesta astme naitaja m: "))
# i = 1
# while i**m <= n**3:
#     print(f"{i}^{m} = {i**m}")
#     i += 1

#Antud on klassi õpilaste füüsika hinded.
#Leia keskmine hinne
#(hinded ja õpilaste arv genereeritakse juhuslikult).

# import random

# n = random.randint(5, 15)
# print("opilaste arv:", n)

# for i in range(n):
#     hinne = random.randint(1, 5)  
#     hinded.append(hinne)

# print("Hinded:", hinded)

# summa = 0
# for hinne in hinded:
#     summa = summa + hinne

# keskmine = summa / n

# print("Keskmine hinne:", round(keskmine, 2))

#Minu rikas onu” kinkis mulle 1 dollari esimesel sünnipäeval
#ja igal järgneval aastal suurendas kingitust nii, 
#et lisas sama palju dollareid, kui vanus oli.
#Kirjuta programm, mis määrab, 
#mitmendaks sünnipäevaks kingitus ületab 100 dollarit.

# kingitus = 0
# vanus = 0
# while kingitus <= 100:
#     vanus += 1
#     kingitus += vanus
#     print(f"Sunnipaevaks number {vanus} uletab kingitus 100 dollarit.")
#     print(f"Kingituse summa on {kingitus} dollarit.")
#     print(f"Kingitus uletab 100 dollarit {vanus}. sunnipaevaks.")


#Kasuta tsüklit, et väljastada Fibonacci jada:
#0 1 1 2 3 5 8 13 21
#(Esimesed kaks arvu on 0 ja 1, iga järgnev on kahe eelmise summa.)

# a , b = 0, 1
# for i in range(200):
#     print(a, end = " ")
#     a, b = b, a + b
#     print()