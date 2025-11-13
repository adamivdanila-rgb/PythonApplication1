
#3. variant
# Kirjuta programm, mis antud arvu n põhjal (1-9) kuvab ekraanile n linnumaja.
# Kahe linnumaja vahel on t�hikurida (t�hikute veerg).
# Lubatud on t�hik p�rast viimast linnumaja.
# Kopeeri linnumaja kuju n�itest arenduskeskkonda
#   -----
#  |  -  |
#  !  -  !
#  *  -  *
#   -----

while True:
    try:
       n=int(input("Sisestage linnumaja arv (1-9): "))
       break
if 1 <= n <= 9:
           

#Väljasta naturaalarvude astmed, mis ei ületa arvu n³.
#Kasutaja määrab astme näitaja ja arvu n.

 n = int(input("Sisesta arv n: "))
 m = int(input("Sisesta astme naitaja m: "))
 i = 1
 while i**m <= n**3:
     print(f"{i}^{m} = {i**m}")
     i += 1

#Antud on klassi õpilaste füüsika hinded.
#Leia keskmine hinne
#(hinded ja õpilaste arv genereeritakse juhuslikult).

 import random

 n = random.randint(5, 15)
 print("opilaste arv:", n)
 for i in range(n):
     hinne = random.randint(1, 5)  
     hinded.append(hinne)
 print("Hinded:", hinded)
 summa = 0
 for hinne in hinded:
     summa = summa + hinne

 keskmine = summa / n

 print("Keskmine hinne:", round(keskmine, 2))

#Minu rikas onu” kinkis mulle 1 dollari esimesel sünnipäeval
#ja igal järgneval aastal suurendas kingitust nii, 
#et lisas sama palju dollareid, kui vanus oli.
#Kirjuta programm, mis määrab, 
#mitmendaks sünnipäevaks kingitus ületab 100 dollarit.

 kingitus = 0
 vanus = 0
 while kingitus <= 100:
     vanus += 1
     kingitus += vanus
     print(f"Sunnipaevaks number {vanus} uletab kingitus 100 dollarit.")
     print(f"Kingituse summa on {kingitus} dollarit.")
     print(f"Kingitus uletab 100 dollarit {vanus}. sunnipaevaks.")


#Kasuta tsüklit, et väljastada Fibonacci jada:
#0 1 1 2 3 5 8 13 21
#(Esimesed kaks arvu on 0 ja 1, iga järgnev on kahe eelmise summa.)

 a , b = 0, 1
 for i in range(200):
     print(a, end = " ")
     a, b = b, a + b
     print()
