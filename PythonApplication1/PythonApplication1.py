#4
#Puu läbimõõdu arvutamine
#Kirjuta programm, 
#mis küsib kasutaja käest puu ümbermõõdu
#ning teatab selle peale puu läbimõõdu.
from math import *
ümbermõõt=int(input("Sisesta puu ümbermõõt meetrites: ")) #int teisendab stringi täisarvuks

läbimõõt=ümbermõõt/3.14 #labimõõt=ümbermõõt/3.14
print(f"Puu läbimõõt on {läbimõõt: ,2f} meetrit") #.2f tähendab 2 kohta pärast koma)




#3
# enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik).
#  Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta.
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile,
#  kui palju komme laual nüüd on. 
from random import *
laua_peal=randint(10.,50) #juhuslik arv
print(f"Laual on {laua_peal} komm")
võtab=int(input("Mitu kommi soovid laualt ära võtta? ")) #sisend võtab stringi täisarveks
laua_peal=võtab #laua_peal-võtab, võtab kommid laualt maha
print(f"Laualmon nüüd {laua_peal} kommi")


# 2.
#Mis tüüpi on järgnevad muutujad:
#a) vanus = 18
#b) eesnimi = "Jaak"
#c) pikkus = 16.5
#d) kas_käib_koolis = True
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.
vanus = 18        #int
eesnimi = "Jaak"  #str
pikkus = 1.65     #float
kas_käib_koolis = True #bool
print(f"vanus (vanus) on: {type(vanus)}")
print(f"eesnimi {eesnimi} on:{type(eesnimi)} ")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}

#Harjutus 1.1. Muutujad ja sisend
#1.
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print("Tere maailm!")
nimi=input("Sisesta oma nimi: ")capitalize()#sisend ja ootab enterit
print(f"Tere maailm! Tervitan sind {nimi}")
vanus=int(input("Sisesta oma vanus: "))#int teisendab stringi
print(f"Tere maailm! Tervitan sind {nimi.upper()}. Sa oled {vanus} aastat vana") #upper teeb suurused
print(f"Tere maailm! Tervitan sind {nimi.upper()}. Sa oled {vanus} aastat vana") #lower 
