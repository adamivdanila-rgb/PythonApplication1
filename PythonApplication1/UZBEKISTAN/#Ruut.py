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


#14 Busside logistika

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
