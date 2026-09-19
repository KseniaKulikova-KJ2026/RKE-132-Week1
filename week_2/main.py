#Programm "Veejoomise kalkulaator"
#Arstid soovitavad juua päevas 2 liitrit vett.
#Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
#Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
#Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
#Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
#Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“


#Alusta programmi.
#Küsi kasutajalt: "Kui palju klaase vett olete juba joonud? (üks klaas = 250 ml)".
#Salvesta vastus muutujasse glasses.
#Arvuta, mitu protsenti päevanormist on täidetud.
#Kui protsent < 50, siis väljasta ekraanile: "Joo rohkem vett, keha vajab seda!"
#Kui protsent < 100, siis väljasta ekraanile: "Tubli, jätka samas vaimus!"
#Kui protsent ≥ 100, siis väljasta ekraanile: "Suurepärane, oled oma päevase eesmärgi täitnud!"
#Lõpeta programm.

goal = 2000
glasses = int(input("Kui palju klaase vett olete juba joonud? (üks klaas = 250 ml) "))
consumed = glasses * 250
percentage = (consumed / goal) * 100

if percentage < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percentage < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
