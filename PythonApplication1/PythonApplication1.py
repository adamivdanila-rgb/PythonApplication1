








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



#1. Juku
#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)
#<6 aastad  - tasuta
#     6-14 - lastepilet
#     15-65 - täispilet
#     >65 - sooduspilet
#     <0 ja >100 viga andmetega

# from curses.ascii import isalpha


# eesnimi=input("Sisesta eesnimi: ")
# if eesnimi=="JUKU":
#     print("Lähme Jukuga kinno!")
#     vanus=input("Sisesta Juku vanus: ")
#     if vanus.isdigit():
#         vanus=int(vanus)
#         if vanus<0 or vanus>100:
#             print("Viga andmetaga!")
#         elif vanus<6:
#             print("Pilet on tasuta!")
#         elif vanus<=14:
#             print("Lastepilet")
#         elif vanus<=65:
#             print("Sooduspilet")
#         else:
#             print("Täispilet")
#     else:
#         print("Palun sisesta vanus täisarvuna!")

#2 Pinginaabrid

#Küsi kahe inimese nimed. Kui nimed koosnevad
# ainult tähedest siis  teavita kasutajat,
#  kas nad on täna pinginaabrid või ei mitte.

# nimi1 = input("Sisesta nimi => ")
# nimi2 = input("Sisesta nimi => ")
# if nimi1.isalpha() and nimi2.isalpha():
#     if nimi1=="Danil" and nimi2=="Nikita" or nimi1=="Nikita" and nimi2=="Danil":
#         print(f"{nimi1} ja {nimi2} on täna pinginaabrid!")
#     else:
#         print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid!")
# else:
#      print("Palun sisesta ainult tähted")


#3 Remont
#Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
#Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.

# pikk = int(input("Sisestage pikkus: "))
# laius = int(input("Sisestage laius: "))
# if pikkus>0 and laius>0:

#     pindala = pikkus * laius
#     print(f"pindala suurus on {pindala}")  
#     user = input("Kas sovite remondi teha? ").capitalize()
#     if user.isalpha() and user == "Jah":
#         hind = float(input("Ruutmeetri hind? "))
#         if hind>0:
#          remondi_hind = hind * pindala
#         print(f"remondi summa on {remondi_hind}")
#         kes = input("Kes teeb remondi(ise/töötaja)? ").capitalize()
#         if kes.isalpha() and kes == "Ise":
#             print(f"Siis summa on {remondi_hind} ")
#         else:
#             print(f"Siis summa on {remondi_hind +300} ")
#     else:
#         print("Hind ei saa olaa negatiivne!")
# else:
#         print("Head aega!")
#      else:
#          print("Arvud paevad olema suurem kui 0!")

     #4 Allahindus
    # Leia 30% soodustusega hinna, kui alghind on suurem kui 700
# from curses.ascii import isdigit

# hind = input("Hind: ")

# if hind.isdigit():
#     hind = float(hind)
#     if hind > 700:
#         hind *= 0.7
#         print(f"Soodushind on {hind}")
# else:
#     print("On vaja numbri sissestada")






#5 Temperatuur

#Küsi temperatuur ning teata,
#Kas see on üle 18 kraadi (soovitav toasoojus talvel)

# try:
#     t=float(input("Sisesta temperatuur: "))
#     if t>18:
#         print("Soovitatav toasoojus talvel")
#     else:
#         print("Võib olla jahe")
# except:
#      print("Palun sisesta temperatuur ujukomaarvuna!")


#6 Pikkus

#Küsi inimese pikkus ning teata, kas ta on lühike,
# keskmine või pikk (piirid pane ise paika)

# try:
#     pikkus = float(input("Sisesta oma pikkus cm: "))
#     if pikkus <= 150:
#         print("Olete lühike")
#     elif pikkus <= 185:
#         print("Olete keskmine")
#     elif pikkus < 185:
#         print("Olete pikk")
#     else:
#       print("Palun sisesta pikkus numbrina!")
# except:
#     print("Sisesta numbrid!" )




#7 Pikkus ja sugu

#Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike,
# keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

# try:
#     pikkus = float(input("Sisesta pikkus cm: "))
#     sugu = input("Sisesta sugu (mees/naine): ").lower()
#     if sugu == "mees":
#         if pikkus <= 160 and pikkus > 0:
#             print("Oled lühike")
#         elif pikkus <= 190 and pikkus > 0:
#             print("Oled keskmine")
#         elif pikkus <= 190 and pikkus > 0:
#             print("Oled pikk")
#     if sugu == "naine":
#         if pikkus <= 150 and pikkus > 0:
#             print("Oled lühike")
#         elif pikkus <= 175 and pikkus > 0:
#             print("Oled keskmine")
#         elif pikkus > 175 and pikkus > 0:
#             print("Oled pikk")
# except:    
#         pass

#8 Poes

#Küsi inimeselt poes eraldi kas ta soovib osta piima,
#saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta,kui tahad.
# Teata, mis summa maksma läheb(Kuva ekraanil tšekk).


#9Ruut
#Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

#print("Sisesta nelja külje pikkused:")

#a = float(input("Külg 1: "))
#b = float(input("Külg 2: "))
#c = float(input("Külg 3: "))
#d = float(input("Külg 4: "))

#if a == b == c == d:
#    print("See on ruut!")
#else:
#    print("See ei ole ruut!")



#11 Juubel
#Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#Plokkskeemi pole vaja!

#praegu = 2025
#sunniaasta = int(input("Sisesta oma sünniaasta: "))
#vanus = praegu - sunniaasta
#if vanus > 0 and vanus % 10 == 0:
#   print(f"Palju õnne! Sul on {vanus} aastat – see on juubel!")
#else:
#    print(f"Sul on {vanus} aastat. Juubelit täna ei tähistata.")



#12 Müük
#Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
#Kuva toote lõplik hind. Plokkskeemi pole vaja!
#hind = float(input("Sisesta toote hind (€): "))

#hind = float(input("Sisesta toote hind (€): "))
#if hind <= 10:
#    soodus = hind * 0.10      
#    loplik_hind = hind - soodus
#    print(f"Allahindlus: 10% ({soodus:.2f} €)")
#else:
#    soodus = hind * 0.20
#    loplik_hind = hind - soodus
#    print(f"Allahindlus: 20% ({soodus:.2f} €)")
#print(f"Lõplik hind: {loplik_hind:.2f} €")


#Busside logistika

#Olgu meil vaja transportida teatud arv inimesi bussidega,
#  milles on teatud arv kohti. Mitu bussi on vaja selleks, 
# et kõik inimesed kohale saaksid,
# ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjuta programm,
#  mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande.

#inimesed = int(input("Mitu inimest vaja transportida? "))
#kohad_bussis = int(input("Mitu kohta on ühes bussis? "))

#if kohad_bussis <= 0:
#   print("Viga: bussis peab olema vähemalt 1 koht!")
#else:
#   if inimesed == 0:
#       busside_arv = 0
#       viimases = 0
#   else:
#          viimases = kohad_bussis  
#
#   print(f"Vaja läheb {busside_arv} bussi.")
#    if busside_arv > 0:
#        print(f"Viimases bussis sõidab {viimases} inimest.")
