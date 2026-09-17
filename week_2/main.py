#Alusta programmi.
#Küsi kasutajalt: "Mis päev on homme? (tööpäev/puhkepäev)".
#Salvesta vastus muutujasse day.
#Kui day on võrdne "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!".
#Kui day on võrdne "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist"
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Vale väärtus".
#Lõpeta programm.

day = input("Mis päev on homme? (tööpäev/puhkepäev): ")
if day == "tööpäev":
    print("Ma lähen magama, head ööd!")    
elif day == "puhkepäev":
    print("Veel üks osa Netflixist")
else:
    print("Vale väärtus")