#Programm "Tervitus"
#Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
#Programm tervitab kasutajat vastavalt soole:
#Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
#Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
#Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“

#Alusta programmi.
#Küsi kasutajalt: "Mis on Teie perekonnanimi?".
#Salvesta vastus muutujasse last_name.
#Küsi kasutajalt: "Mis on Teie sugu? (m/n)".
#Salvesta vastus muutujasse gender.
#Kui gender on "m", siis väljasta ekraanile: "Tere, härra [last_name]!"
#Kui gender on "n", siis väljasta ekraanile: "Tere, proua [last_name]!"
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Tere tulemast, [last_name]!"
#Lõpeta programm.



last_name = input("Mis on Teie perekonnanimi? ")
gender = input("Mis on Teie sugu? (m/n) ")

if gender == "m":
    print("Tere, härra", last_name, "!")
elif gender == "n":
    print("Tere, proua", last_name, "!")
else:
    print("Tere tulemast,", last_name, "!" )